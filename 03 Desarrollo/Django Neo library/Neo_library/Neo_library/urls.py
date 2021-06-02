
from django.contrib import admin
from django.urls import path
from prestamos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('log_admin',views.log_admin,name='log_admin'),
    path('login_user',views.log_user,name='log_user'),
    path('administracion',views.administration,name='administration'),
    path('mis_prestamos',views.my_loans,name='mis_prestamos'),
    path('prestamos',views.loans,name='prestamos'),
    path('users',views.users,name='usuarios'),
    path('books',views.books,name='libros')
]
