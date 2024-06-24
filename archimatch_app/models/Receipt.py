from archimatch_app.models import BaseModel
from django.db import models
from .user.Architect import Architect



class Receipt(BaseModel):
    architect = models.ForeignKey(Architect, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=255)
    date_of_transaction= models.DateField()
    sub_purchased = models.CharField(max_length=255)
    amount_paid = models.FloatField()
    


    def __str__(self):
        return self.email
