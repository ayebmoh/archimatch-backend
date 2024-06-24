from django.db import models
from .BaseModel import BaseModel
from archimatch_app.models.utils.Report import Report

class ArchiReport(BaseModel):
    architect = models.OneToOneField('Architect', on_delete=models.CASCADE, related_name="Archireports", null=True)
    status = models.CharField(max_length=255,default="Non-traité")
    rep_count = models.IntegerField(default=0)
    reports = models.ManyToManyField(Report, related_name="Arhcireports")

    def __str__(self):
        return self.status
