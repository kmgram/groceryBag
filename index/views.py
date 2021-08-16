from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreation, ModelFormGroceryList
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import GroceryList


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard-view')
    else:  
        if request.method == "POST":
            form = CustomUserCreation(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been created successfully!,\
                 login to proceed further')
                return redirect('login-view')
        form = CustomUserCreation()
        context = {'form': form}
        return render(request,'index/register.html',context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard-view')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)                
                return redirect('dashboard-view')
            else:
                messages.info(request, 'Login attempt failed; username or password incorrect')
        return render(request,'index/login.html')

def logout_user(request):
    logout(request)
    return redirect('login-view')

@login_required(login_url = '/login')
def dashboard(request):
    if request.method == 'POST':        
        date_to_filter = request.POST.get('date_select')
        if date_to_filter:                
            querydata = GroceryList.objects.filter(date_created=date_to_filter,user=request.user)       
            return render(request,'index/dashboard.html', {'querydata':querydata})
        else:
            messages.warning(request,'Select the date before applying filter')
            querydata = GroceryList.objects.filter(user=request.user)
            return render(request,'index/dashboard.html', {'querydata':querydata})
       
    else:        
        querydata = GroceryList.objects.filter(user=request.user)
        return render(request,'index/dashboard.html', {'querydata':querydata}) 
   
    
@login_required(login_url = '/login')
def add_item(request):
    if request.method == 'GET':
        form_grocery = ModelFormGroceryList()
        return render(request, 'index/add.html',{'form_grocery': form_grocery})
    elif request.method == 'POST':        
        data_mdfy = ModelFormGroceryList(request.POST)
        if data_mdfy.is_valid():                  
            item_name_request = (request.POST.get('name'))
            item_name_db = GroceryList.objects.filter(name=item_name_request,user=request.user)         
            if GroceryList.objects.filter(name__iexact=item_name_request,user=request.user):
                messages.error(request, f'{item_name_request} is already present in the list,\
                    use "Update" button on dashboard to modify the list')
                return redirect('add-view')
            else:                
                obj=data_mdfy.save(commit=False)
                obj.user=request.user
                obj.save()            
                messages.success(request, 'Your request to add item is successful')
                return redirect('dashboard-view')
        else:
            form_grocery = ModelFormGroceryList(request.POST)
            messages.error(request, 'Data validation failed, input correct details')
            return render(request, 'index/add.html',{'form_grocery': form_grocery})
            
            



@login_required(login_url = '/login')
def update_item(request,input_arg=''):
    if request.method == 'GET':
        if input_arg:
            obj_db = GroceryList.objects.get(id=input_arg)
            form_instance = ModelFormGroceryList(instance=obj_db)
            return render(request,'index/update.html', {'form_instance': form_instance})
    elif request.method == 'POST':
        obj_db = GroceryList.objects.get(id=input_arg)
        form_instance = ModelFormGroceryList(request.POST,instance=obj_db)
        form_instance.user = request.user       
        if form_instance.is_valid():                                  
            form_instance.save()
            messages.success(request, 'Your request to update item is successful')
            return redirect('dashboard-view')
        else:
            
            messages.error(request, 'Data validation failed, input correct details')
            return render(request, 'index/update.html',{'form_instance': form_instance})


@login_required(login_url = '/login')
def delete_item(request,input_arg=''):
    if request.method == 'GET':
        if input_arg:
            obj_db = GroceryList.objects.get(id=input_arg)            
            return render(request,'index/delete.html', {'form_instance': obj_db})
    if request.method == 'POST':
        delete_db_obj = GroceryList.objects.get(id=input_arg)        
        delete_db_obj.delete()
        messages.success(request, 'Your request to delete item is successful')
        return redirect('dashboard-view')




def add_update(request,input_arg=''):
    if request.method == 'GET':
        if input_arg == 'add':
            return render(request,'index/add.html')
        elif input_arg == 'update':
            return render(request,'index/update.html')
        elif input_arg == 'delete':
            return render(request,'index/delete.html')


