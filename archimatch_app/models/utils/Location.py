from django.db import models
from .BaseModel import BaseModel
    
class Location(BaseModel):
    display = models.CharField(max_length=255)

    def __str__(self):
        return self.display