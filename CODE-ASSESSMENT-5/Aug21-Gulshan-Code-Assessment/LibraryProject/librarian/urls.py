from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('register',views.register,name="librarian_register"),
    path('login',views.login,name="librarian_login"),
    path('add/',views.lib_add,name="Add_data"),
    path('viewall/',views.all_lib,name="viewall_data"),
    path('view/<id>',views.update,name="update_data"),
    path('enroll_code/<enroll_code>',views.search_By_enroll_code,name="view_data_by_enroll_code"),
]