
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from prestamos import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login_user',views.log_user,name='log_user'), 
    path('administracion',views.administration,name='administration'),
    path('mis_prestamos/user/<int:Cliient_id>/',views.my_loans,name='mis_prestamos'),#vista a mis prestamos, (probando)
    path('prestamos',views.loans,name='prestamos'),
    path('users',views.users,name='usuarios'), # probando
    path('books',views.books,name='libros'),
    path('register',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('infolibro/book/<int:Book_id>',views.booksinfo,name='infolibro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)