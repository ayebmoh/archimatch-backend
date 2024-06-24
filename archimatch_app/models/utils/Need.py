from django.db import models

from .BaseModel import BaseModel

class NeedElement(BaseModel):
    display = models.CharField(max_length=255)
    def __str__(self):
        return self.display
    
class Need(BaseModel):
    display = models.CharField(max_length=255)
    icon = models.ImageField(blank=True,null=True,upload_to='BesoinsIcons/')
    elements = models.ManyToManyField(NeedElement, related_name='exemples')
    def __str__(self):
        return self.display