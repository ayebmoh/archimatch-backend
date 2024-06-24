from django.db import models
from .BaseModel import BaseModel
    
class Worksurface(BaseModel):
    display = models.CharField(max_length=255)

    def __str__(self):
        return self.display