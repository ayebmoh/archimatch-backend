from django.db import models
from .BaseModel import BaseModel
from django.core.validators import MaxValueValidator

class Subscription(BaseModel):
    sub_name = models.CharField(max_length=255,)
    prop_platform =models.BooleanField(default=True)
    prop_profil =models.BooleanField(default=False)
    realization_expo =models.BooleanField(default=False)
    prop_selon_pref =models.BooleanField(default=False)
    mev_profil =models.BooleanField(default=False)
    archi_supp =models.BooleanField(default=False)
    fournisseur =models.BooleanField(default=False)
    devi_gen =models.BooleanField(default=False)
    token_num = models.IntegerField(validators=[MaxValueValidator(50)])
    price = models.FloatField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.sub_name