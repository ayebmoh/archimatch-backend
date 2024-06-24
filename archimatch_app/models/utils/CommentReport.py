from django.db import models
from .BaseModel import BaseModel
from archimatch_app.models.utils.Report import Report

class CommentReport(BaseModel):
    comment = models.OneToOneField('Comment', on_delete=models.CASCADE, related_name="commet_report", null=True)
    status = models.CharField(max_length=255,default="Non-traité")
    rep_count = models.IntegerField(default=0)
    reports = models.ManyToManyField(Report, related_name="comments_report")

    def __str__(self):
        return self.status
