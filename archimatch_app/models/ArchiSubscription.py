from django.db import models
from .utils.BaseModel import BaseModel
from django.core.validators import MaxValueValidator

class ArchiSubscription(BaseModel):
    sub_name = models.CharField(max_length=255,default="")
    free_tokens = models.IntegerField(validators=[MaxValueValidator(50)],default=0)
    price = models.FloatField(default=0.0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.sub_name