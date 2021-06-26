from django.test import TestCase
from django.urls import reverse

class testviews (TestCase):

    def test_index_view_correct (self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'index.html')

    def test_administration_view_correct (self):
        resp = self.client.get(reverse('administration'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'administracion.html')

    def test_mis_prestamos_view_correct (self):
        resp = self.client.get(reverse('mis_prestamos'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'mis_prestamos.html')

    def test_log_admin_view_correct (self):
        resp = self.client.get(reverse('log_admin'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'loginad.html')

    def test_log_user_view_correct (self):
        resp = self.client.get(reverse('log_user'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'loginus.html')

    def test_prestamos_view_correct (self):
        resp = self.client.get(reverse('prestamos'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'prestamos.html')

    def test_usuarios_view_correct (self):
        resp = self.client.get(reverse('usuarios'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'usuarios.html')

    def test_libros_view_correct (self):
        resp = self.client.get(reverse('libros'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'libros.html')
