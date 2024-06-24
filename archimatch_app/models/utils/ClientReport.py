from django.db import models
from .BaseModel import BaseModel
from archimatch_app.models.utils.Report import Report
from archimatch_app.models.user.Client import Client

class ClientReport(BaseModel):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name="Clientreport", null=True)
    status = models.CharField(max_length=255,default="Non-traité")
    rep_count = models.IntegerField(default=0)
    reports = models.ManyToManyField(Report, related_name="Clientreport")

    def __str__(self):
        return self.status
