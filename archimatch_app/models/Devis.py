from django.db import models
from archimatch_app.models.utils.BaseModel import BaseModel
from archimatch_app.models import Architect


class Devis(BaseModel):
    file = models.FileField(blank=True,null=True,upload_to='Devis/')
    status = models.CharField(max_length=255,default="Pending")
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE,related_name="devis_architect", blank=True, null=True)
    def __str__(self):
        return self.status