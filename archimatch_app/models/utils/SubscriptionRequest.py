from archimatch_app.models.utils.BaseModel import BaseModel
from django.db import models





class SubscriptionRequest(BaseModel):
    arch_id = models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    sub_name =models.CharField(max_length=255)
    request_date=models.DateTimeField()
    active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.email

    
    
