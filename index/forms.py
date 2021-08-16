from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from . models import GroceryList

class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class ModelFormGroceryList(forms.ModelForm):
    class Meta:
        model = GroceryList
        fields = ['name', 'quantity','qty_unit','status','date_created']
        widgets = {
            'date_created' : forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control','placeholder':'Select a date', 'type':'date'}),
           'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Item name',}),
           'quantity' : forms.TextInput(attrs={'class':'form-control','placeholder':'Item quantity--Non negative value',}),
           'qty_unit' : forms.Select(attrs={'class':'regDropDown','style' : 'width:400px'}),
        }
        


        

    def __init__(self,*args,**kwargs):
        super(ModelFormGroceryList,self).__init__(*args,**kwargs)
        self.fields['status'].empty_label = 'Select'
