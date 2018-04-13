from django.db import models

from account import models as account_model


#farm product
class Product(models.Model):
    user = models.ForeignKey(account_model.UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    contact_period = models.FloatField(null=True, blank=True)
    expected_return = models.FloatField(null=True, blank=True)
    harvest_period = models.FloatField(null=True, blank=True)

    price = models.FloatField(null=True, blank=True)

    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    extra = models.TextField(max_length=5000, null=True, blank=True)

    farm_size = models.FloatField(null=True, blank=True)
    farm_location = models.TextField(max_length=1000, null=True, blank=True)

    product_type = models.CharField(max_length=255, null=True, blank=True)

    farm_email = models.EmailField(max_length=255, null=True, blank=True)

    product_image = models.ImageField(upload_to='product/', default='/media/no-img.jpg', null=True, blank=True)


    def __str__(self):
        return self.name + "-" + self.farm_email
