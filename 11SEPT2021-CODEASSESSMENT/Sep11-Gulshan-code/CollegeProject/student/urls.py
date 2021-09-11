from . import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('profile/',views.register,name='register'),
    # path('search/',views.search,name='search'),
    path('logincheck/', views.login_check, name= 'login_check'),

    path('add/',views.student,name='student'),
    path('viewall/',views.student_list,name='student_list'),
    path('dashboard',views.dashboard,name='studentdetail'),
    path('update',views.updatesearchapi,name='studentdetail'),
    path('updatedata',views.update_data_read,name='studentdetail'),
    
]
