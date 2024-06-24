from django.db import models
from .BaseModel import BaseModel
    
class Right(BaseModel):
    display = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=5)

    def __str__(self):
        return self.display