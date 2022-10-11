from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=150)
    pub_date = models.DateField()