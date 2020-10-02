from django.test import TestCase


class ViewTest(TestCase):

    def test_help(self):
        self.assertTrue(True)

    def test_root_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 201)

    def test_root_title(self):
        response = self.client.get('/')
        self.assertContains(response, '<Title> eshoppning </Title>')
    
    def test_cart_page(self):
        response = self.client.get('/cart')
        self.assertEqual(response.status_code, 202)

    def test_cart_template(self):
        response = self.client.get('/cart')
        self.assertTemplateUsed(response, template_name='cart.html')

    def test_checkout_page(self):
        response = self.client.get('/checkout')
        self.assertEqual(response.status_code, 203)
    
    def test_checkout_template(self):
        response = self.client.get('/checkout')
        self.assertTemplateUsed(response, template_name='checkout.html')

    def test_store_page(self):
        response = self.client.get('/store')
        self.assertEqual(response.status_code, 204)
    
    def test_store_template(self):
        response = self.client.get('/store')
        self.assertTemplateUsed(response, template_name='store.html')
    
    def test_admin_page(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 205)
    
    def test_admin_template(self):
        response = self.client.get('/admin')
        self.assertTemplateUsed(response, template_name='admin.html')
    
    def test_fake_page(self):
        response = self.client.get('/fake')
        self.assertEqual(response.status_code, 206)
    
    def test_fake_template(self):
        response = self.client.get('/fake')
        self.assertTemplateUsed(response, template_name='fake.html')

class ModelsTest(TestCase):

    def test_help(self):
        self.assertTrue(True)