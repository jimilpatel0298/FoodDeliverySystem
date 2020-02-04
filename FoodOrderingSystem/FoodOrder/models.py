from djongo import models
from django.contrib.auth import get_user_model
from djongo import models as model

class Product(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    amount = models.PositiveIntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='fooditems/', blank=True, null=True, default='fooditems/noimage.png')

    def __str__(self):
        return self.title


class TotalOrders(models.Model):
    title = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()


class Orders(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    orders= model.ArrayField(
        model_container=TotalOrders
    )
