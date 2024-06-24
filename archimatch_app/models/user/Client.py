from django.db import models
from .ArchimatchUser import ArchimatchUser
from django.core.exceptions import ValidationError
from archimatch_app.models.utils.BaseModel import BaseModel

class Client(BaseModel):
    user = models.OneToOneField(ArchimatchUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    
    
    class Meta:
        verbose_name_plural = "Clients"