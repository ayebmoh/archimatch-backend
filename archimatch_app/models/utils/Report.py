from django.db import models
from archimatch_app.models.user.ArchimatchUser import ArchimatchUser
from .BaseModel import BaseModel


class Report(BaseModel):
    user = models.ForeignKey(ArchimatchUser,related_name="Reports",on_delete=models.CASCADE,default=2)
    description = models.CharField(max_length=255)


    def __str__(self):
        return self.description