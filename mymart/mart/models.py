from distutils.command.upload import upload
from statistics import mode
from django.db import models
from traitlets import default

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50, default='')
    sub_category = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=150)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='mart/images', default='')

    def __str__(self):
        return self.product_name
