from django.db import models
from .BaseModel import BaseModel

class BankCard(BaseModel):
    card_num = models.IntegerField()
    card_holder = models.CharField(max_length=255, null=True, blank=True,default='')
    cvv = models.IntegerField()
    expiration_date = models.DateField()

    def __int__(self):
        return self.card_num