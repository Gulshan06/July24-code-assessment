from django.urls import path,include
from.import views
urlpatterns=[
    
    path("adddd/",views.doctor,name="doctor"),
    path("viewalld/",views.doctorlist,name="doctorlist"),
    path("viewd/<fetchid>",views.mydoctors,name="mydoctors"),
    path('searchd/', views.search_customer, name='search_customer'), 
    path('updateapi/', views.update_api, name='update_api'), 
    path('updatedata/', views.update_data, name='update_data'),
    path('deleteapi/', views.delete_api, name='delete_api'), 
    path('deletedata/', views.delete_data, name='delete_data'),






    path('header/',views.head,name="head"),
    path('add/', views.add_d, name='add_d'),
    path('view/', views.view_d, name='view_d'),
    path('search/', views.search_d, name='search_d'),
    path('update/', views.update_d, name='update_d'),
    path('delete/', views.delete_d, name='delete_d'),


]

