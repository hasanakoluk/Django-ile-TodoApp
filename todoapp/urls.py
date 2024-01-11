from django.urls import path
from .views import *

urlpatterns = [
    path('',todo_anasayfa,name="todo_page"),
    path('kategori/<slug:kategori_slug>',kategori_view,name="kategori_page"),
    path('detay/<slug:todo_slug>',detay_view,name = "detay_page"),
    path('todo-add/',todo_ekle_view,name="todo_ekle_page"),
    path('todo-edit/<slug:todo_slug>/',todo_edit_view,name="todo_edit_page"),
    path('todo-delete<slug:todo_slug>/',todo_delete_view, name="todo_delete_page"),
    path('alt_kategori/<slug:alt_kategori_slug>',alt_kategori_view,name="alt_kategori_page"),

    
]

