from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User
from eshop.models import Order

from eshop.utils import cartData
from eshop.views import cart


class ViewTest(TestCase):

    def test_root_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 201)

    def test_root_title(self):
        response = self.client.get('/')
        self.assertContains(response, '<Title> eshoppning </Title>')
    
    def test_cart_page(self):
        response = self.client.get('cart')
        self.assertEqual(response.status_code, 202)

    def test_cart_template(self):
        response = self.client.get('cart')
        self.assertTemplateUsed(response, template_name='cart.html')

    def test_checkout_page(self):
        response = self.client.get('checkout')
        self.assertEqual(response.status_code, 203)
    
    def test_checkout_template(self):
        response = self.client.get('checkout')
        self.assertTemplateUsed(response, template_name='checkout.html')

    def test_store_page(self):
        response = self.client.get('store')
        self.assertEqual(response.status_code, 204)
    
    def test_store_template(self):
        response = self.client.get('store')
        self.assertTemplateUsed(response, template_name='store.html')
    
    def test_admin_page(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 205)
    
    def test_admin_template(self):
        response = self.client.get('/admin')
        self.assertTemplateUsed(response, template_name='admin.html')
    
    def test_help(self):
        self.assertTrue(True)

class ModelsTest(TestCase):

    def test_Customer(self):
        Customer.objects.create(user='Vice', name='Vicente', email= 'test@gmail.com')
        x = Customer.objects.get(pk=1)
        self.assertEqual(x.user, 'Vice')
        self.assertEqual(x.name, 'Vicente')
        self.assertEqual(x.email, 'test@gmail.com')

    def test_product(self):
        Product.objects.create(name='Guitar', price=500, digital= False)
        x = Product.objects.get(pk=1)
        self.assertEqual(x.name, 'Guitar')
        self.assertEqual(x.price, 500)
        self.assertEqual(x.digital, False)
    
    def test_Order(self):
        Order.objects.create(customer='Bruce', complete= False, transaction_id= 56178)
        x = Order.objects.get(pk=1)
        self.assertEqual(x.customer, 'Bruce')
        self.assertEqual(x.complete, False)
        self.assertEqual(x.transaction_id, 56178)
    
    def test_OrderItem(self):
        OrderItem.objects.create(product='Shirt', order=8, quantity= 2)
        x = OrderItem.objects.get(pk=1)
        self.assertEqual(x.product, 'Shirt')
        self.assertEqual(x.order, 8)
        self.assertEqual(x.quantity, 2)
    
    def test_Shipping(self):
        ShippingAddress.objects.create(Customer='Rick', order=6, address= '123 drive st', city='Denver', state='CO', zipcode=80123,)
        x = ShippingAddress.objects.get(pk=1)
        self.assertEqual(x.customer, 'Rick')
        self.assertEqual(x.order, 6)
        self.assertEqual(x.address, '123 drive st')
        elf.assertEqual(x.city, 'Denver')
        elf.assertEqual(x.state, 'CO')
        elf.assertEqual(x.zipcode, '80123')

    def test_help(self):
        self.assertTrue(True)

class GuestCheckoutTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_guest_cart(self):
        cook = {1:{'quantity': 1}, 2:{'quantity': 1}, 3:{'quantity': 1}}

        request = self.factory.get('/cart')
        request.test_cart = cook
        request.user = User
        request.user.is_authenticated = False

        response = cart(request)

        self.assertEqual(response.status_code, 200) # Make sure everything comes back OK
        

