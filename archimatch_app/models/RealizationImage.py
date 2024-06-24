from archimatch_app.models import BaseModel
from django.db import models
from .Realization import Realization



class RealizationImage(BaseModel):
    realization = models.ForeignKey(Realization, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(blank=True,null=True,upload_to='realizations/')
    


    def __str__(self):
        return str(self.id)
    