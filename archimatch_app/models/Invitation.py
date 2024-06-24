from django.db import models

from archimatch_app.models.utils.BaseModel import BaseModel
from archimatch_app.models.user.Architect import Architect
from .user.Client import Client


class Invitation(BaseModel):
    
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE,related_name="architect_inv",blank=True,null=True)
    invited_email = models.CharField(max_length=255, null=True, blank=True,default='')
    status = models.CharField(max_length=255, null=True, blank=True,default='Pending')
    
    

    def __str__(self):
        return str(self.invited_email)

