from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    #We will not do a relationship between Contact and Listing,
    #because no need to do so as we only need title of the listing and the id
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True) #optional field
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True) 
    #people who has not loged in to inquire will be blank
    def __str__(self): #double underscore
        return self.name
        # Define main field to be displayed in admin area, which is title