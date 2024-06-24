from django.db import models
from django.utils import timezone
from datetime import timedelta
from archimatch_app.models.utils.BaseModel import BaseModel
from archimatch_app.models.user.Architect import Architect
from .Announcement import Announcement
from .Devis import Devis

class Selection(BaseModel):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE,related_name="selections",blank=True, null=True)
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE,related_name="selections",blank=True,null=True)
    devis = models.ManyToManyField(Devis, related_name='Selections')
    interested_architects = models.ManyToManyField(Architect,related_name="interested_architects", blank=True)
    expiration_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.announcement)

    def save(self, *args, **kwargs):
        if not self.expiration_date:
            self.expiration_date = self.created_at + timedelta(days=5)
        super().save(*args, **kwargs)
