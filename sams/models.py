from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ExtendedData(models.Model):
    TYPE_CHOICES = [("B","Comprador"), ("R","Replenisher")]
    user_type = models.CharField(max_length=1, choices= TYPE_CHOICES)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    def __str__ (self):
        return 'el user_type es: %s' % (self.user_type)  

class Vendor(models.Model):
    vendor_name = models.CharField(max_length= 255)
    vendor_type = models.CharField(max_length= 255)
    created_date = models.DateTimeField(default = timezone.now, blank= True, null = True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    
    def __str__ (self):
        return 'el vendor es: %s %s' % (self.vendor_name, self.vendor_type)