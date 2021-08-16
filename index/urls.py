from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'home-view'),
    path('register/', views.registration_page, name = 'registration-view'),
    path('login/', views.login_page, name = 'login-view'),
    path('logout/', views.logout_user, name = 'logout-view'),
    path('dashboard/', views.query_grocery, name = 'dashboard-view'),
    path('additem/', views.add_item, name = 'add-view'),
    path('updateitem/<input_arg>/', views.update_item, name = 'update-view'),
    path('dashboard/<input_arg>/', views.add_update, name = 'add_update-view'),
    path('deleteitem/<input_arg>/', views.delete_item, name = 'delete-view'),
]