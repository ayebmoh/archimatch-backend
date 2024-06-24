from django.db import models
from .utils.BaseModel import BaseModel
from .utils import Worksurface,Worktype,Goodtype,Services,Location,Projectbudget

class Preference(BaseModel):
    work_type = models.ManyToManyField(Worktype,related_name="Preferences")
    good_type = models.ManyToManyField(Goodtype,related_name="Preferences")
    service = models.ManyToManyField(Services,related_name="Preferences")
    location = models.ManyToManyField(Location,related_name="Preferences")
    work_surface = models.ManyToManyField(Worksurface,related_name="Preferences")
    project_budget = models.ManyToManyField(Projectbudget,related_name="Preferences")
    

    def __str__(self):
        return str(self.id)