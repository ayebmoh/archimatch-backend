from archimatch_app.models.utils.BaseModel import BaseModel
from django.db import models
from django.core.exceptions import ValidationError


STATUS_CHOICES = [
    ('Accepted','Accepted'),
    ('Refused','Refused'),
    ('En attente Demo','En attente Demo'),
    ('En attente Decision','En attente Decision'),
]


class ArchitectRequest(BaseModel):
    adresse  = models.CharField(max_length=255, blank=True, null=True)
    arch_identifier = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email=models.EmailField()
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    meeting_date = models.DateTimeField()
    meeting_duration = models.IntegerField(default=30)
    meeting_time = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)
    registration_number = models.CharField(max_length=255)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES, default='En attente Decision')
    architect_type = models.ForeignKey('archimatch_app.ArchitectType',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email

    
    
