from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model): #Way easier to set up db from django than in sql or pgAdmin
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    #foreign ley from another table, need to import from realtors.models.py
    #'on_delete=models.DO_NOTHING': Even you delete the realtor, the listing that associated with will not be deleted
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    #'blank=True': Not Required Field
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    #1.5, 2.5, 3.0
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #allocate files into different date folders under photo
    #anything we upload in admin area like photos or files will go to a media folder in django
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    #'blank=True': optional field
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    #need to import 'from datetime import datetime' to use datetime
    def __str__(self): #double underscore
        return self.title
    # Define main field to be displayed in admin area, which is title

