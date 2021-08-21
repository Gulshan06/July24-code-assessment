from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('',views.add,name="add_book"),
    path('add/',views.add_book,name="Add_book"),
    path('viewall/',views.all_view,name="viewall_book"),
    path('view/<fetchid>',views.update,name="update_book"),
    path('bookname/<bookname>',views.by_bookname,name="view by bookname"),
]