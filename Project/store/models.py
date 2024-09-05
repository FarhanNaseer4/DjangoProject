from django.db import models

class promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('products', on_delete=models.SET_NULL, null=True, related_name='+') # plus will indicate django no circular relation creation

class products(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    lastUpdate = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(promotion)

class customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SLIVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICE = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SLIVER, 'Sliver'),
        (MEMBERSHIP_GOLD, 'GOLD')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, unique=True, default='farhannaseer@hotmail.com')
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICE, default=MEMBERSHIP_BRONZE)

class order(models.Model):
    STATUS_PENDING = 'P'
    STATUS_COMPLETE = 'C'
    STATUS_FAILED = 'F'
    STATUS_CHOICE = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETE, 'Complete'),
        (STATUS_FAILED, 'Failed'),
    ]
    place_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=STATUS_PENDING)
    customer = models.ForeignKey(customer, on_delete=models.PROTECT)

class orderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.PROTECT)
    product = models.ForeignKey(products, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unitPrice = models.DecimalField(max_digits=6, decimal_places=2)

class cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class cartItem(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    

class address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(null=True, max_length=255)
    customer = models.OneToOneField(customer, on_delete=models.CASCADE, primary_key=True) # one to one relation
    # customer = models.ForeignKey(customer, on_delete=models.CASCADE) one to many relation
# Create your models here.
