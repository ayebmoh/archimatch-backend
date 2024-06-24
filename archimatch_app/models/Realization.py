from archimatch_app.models.utils.BaseModel import BaseModel
from django.db import models
from .user.Architect import Architect
from .utils.Category import Category


class Realization(BaseModel):
    architect = models.ForeignKey(Architect, on_delete=models.SET_NULL, null=True)
    categorie = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="Realizations",null=True)
    style = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    surface = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    project_title = models.CharField(max_length=255,blank=True, null=True)


    def __str__(self):
        return self.city
