from django.contrib.auth.models import AbstractUser
from django.db import models
import phonenumbers
from django.core.exceptions import ValidationError

USER_TYPE_CHOICES = [
    ('Architect', 'Architect'),
    ('Client', 'Client'),
    ('Admin', 'Admin'),
    ('Supplier', 'Supplier'),
]

class ArchimatchUser(AbstractUser):
    image = models.ImageField(blank=True, null=True, upload_to='ProfileImages/')
    phone_number = models.CharField(max_length=20, blank=True)
    user_type = models.CharField(max_length=200, choices=USER_TYPE_CHOICES)
    
    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

