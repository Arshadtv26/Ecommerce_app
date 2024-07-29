from django.db import models
from customer.models import Customer
from product.models import Product

# Create your models here.
class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    ORDER_CHOICE = ((ORDER_CONFIRMED,'ORDER_CONFIRMED'),
                    (ORDER_PROCESSED,'ORDER_PROCESSED'),
                    (ORDER_DELIVERED,'ORDER_DELIVERED'),
                    (ORDER_REJECTED, 'ORDER_REJECTED'))
    order_status = models.IntegerField(choices= ORDER_CHOICE, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL,related_name='owner',null=True)
    delete_status = models.IntegerField(choices= DELETE_CHOICE, default= LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return 'Order - {} - {}'.format(self.id, self.owner.name)

class OrderedItem(models.Model):
    product = models.ForeignKey(Product,on_delete = models.SET_NULL, related_name='added_carts',null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='added_items',null=True)


