from django.conf.urls import url
from django.test import TestCase
from django.urls import reverse,resolve
from prestamos.views import index,log_admin,administration,my_loans,loans,users,books,logout_view

class Test_all_Urls (TestCase):

    def test_url_index(self):
        url = reverse ('index')
        self.assertEquals(resolve(url).func,index)
        
    def test_url_log_admin(self):
        url = reverse ('log_admin')
        self.assertEquals(resolve(url).func,log_admin)

    def test_url_administration(self):
        url = reverse ('administration')
        self.assertEquals(resolve(url).func,administration)

    def test_url_mis_prestamos(self):
        url = reverse ('mis_prestamos')
        self.assertEquals(resolve(url).func,my_loans)
    
    def test_url_Prestamos(self):
        url = reverse ('prestamos')
        self.assertEquals(resolve(url).func,loans)

    def test_url_usuarios(self):
        url = reverse ('usuarios')
        self.assertEquals(resolve(url).func,users)

    def test_url_libros(self):
        url = reverse ('libros')
        self.assertEquals(resolve(url).func,books)

    def test_url_logout(self):
        url = reverse ('logout')
        self.assertEquals(resolve(url).func,logout_view)
