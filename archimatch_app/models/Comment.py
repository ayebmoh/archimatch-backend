from django.db import models

from archimatch_app.models.utils.BaseModel import BaseModel
from archimatch_app.models.user.Architect import Architect
from .user.Client import Client


class Comment(BaseModel):
    Client = models.ForeignKey(Client, on_delete=models.CASCADE,related_name="client",blank=True, null=True)
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE,related_name="architect",blank=True,null=True)
    message = models.CharField(max_length=255, null=True, blank=True,default='')
    
    

    def __str__(self):
        return str(self.message)

