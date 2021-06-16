
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Count
from django.conf import settings
from taggit.managers import TaggableManager


# Create your models here.
class Customer(models.Model):
    User            = settings.AUTH_USER_MODEL
    user            = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    shippingAddress = models.ForeignKey('ShippingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    email 			= models.EmailField(verbose_name="email", max_length=60, unique=True, null=True)

    def __str__(self):
        if self.email:
            return self.email
    @property
    def orders(self):
        order_count = self.order_set.all().count()
        return str(order_count)


class Beneficiary(models.Model):
    name                = models.CharField(max_length=200, null=False)
    surname             = models.CharField(max_length=200, null=False)
    email 			    = models.EmailField(verbose_name="email", max_length=60, unique=True, null=True)
    phone_number               = models.CharField(max_length=20, null=False)
    customer            = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL1(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url
    class Meta:
        verbose_name = 'Beneficiery'
        verbose_name_plural = 'Beneficiaries'

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Payment Confirmed, Processing Order', 'Payment Confirmed, Processing Order'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return str(self.customer)

    @property
    def shipping(self):
        shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        allitems = sum([item.quantity for item in orderitems])
        return allitems

class OrderItem(models.Model):
    product = models.ForeignKey(Beneficiary, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    country = models.CharField(max_length=200, null=False)
    address1 = models.CharField(max_length=200, null=False)
    address2 = models.CharField(max_length=200, null=True)
    suburb = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=False)
    province = models.CharField(max_length=200, null=False)
    postal_code = models.CharField(max_length=20, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.country)


class Category(models.Model):
    ## for product category
    category_name       = models.CharField(max_length=50)
    date_added          = models.DateTimeField(auto_now_add=True, null=True)
    date_updated        = models.DateTimeField(auto_now_add=True, null=True)
    slug                = models.SlugField(blank=True, null=True, max_length=150, unique=True, db_index=True)

    def save(self , *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(Category , self).save(*args, **kwargs)

    class Meta:
        ordering = ('-date_added', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
