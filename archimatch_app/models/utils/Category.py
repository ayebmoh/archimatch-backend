from django.db import models
from .BaseModel import BaseModel
from .SubCategory import SubCategory

class Category(BaseModel):
    display = models.CharField(max_length=255)
    sub_categories = models.ManyToManyField(SubCategory, related_name='Categories')

    def __str__(self):
        return str(self.display)