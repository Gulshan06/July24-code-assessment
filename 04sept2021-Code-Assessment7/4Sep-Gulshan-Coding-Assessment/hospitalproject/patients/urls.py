from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('add/', views.addcustomer, name='addcustomer'),
    path('viewall/', views.viewcustomer, name='viewcustomer'),
    path('view/<fetchid>', views.update_d, name='update_d'),
    path('search/', views.search_customer, name='search_customer'), 
    path('updateapi/', views.update_api, name='update_api'), 
    path('updatedata/', views.update_data, name='update_data'),
    path('deleteapi/', views.deleteapi, name='deleteapi'), 
    path('deletedata/', views.delete_data, name='delete_data'),



    path('',views.home,name="homepage"),
    path('main/', views.mainpage, name='mainpage'),
    path('register/', views.add_customer, name='add_customer'),
    path('view/', views.view_customer, name='view_customer'),
    path('searchc/', views.search_c, name='search_c'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('viewprofile', views.prof_view, name='prof_view'),

]