from django.db import models
from .ArchimatchUser import ArchimatchUser
from django.core.exceptions import ValidationError
from ..utils.Right import Right
from archimatch_app.models.utils.BaseModel import BaseModel


class Admin(BaseModel):
    user = models.OneToOneField(ArchimatchUser, on_delete=models.CASCADE)
    super_user = models.BooleanField(default=False)
    rights = models.ManyToManyField(Right, related_name='admins', blank=True, null=True)
    
    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name_plural = "Admins"
    
    
