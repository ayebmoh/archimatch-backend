from django.db import models
from .BaseModel import BaseModel
    
class NeedPieces(BaseModel):
    nb_suite_parental = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_cuisine = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_Terasse =models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_chambre=models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_salle_a_manger=models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_jardin=models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_chambre_enfant=models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_salle_bain=models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_haul=models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_salon=models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_bureau=models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 
    nb_garage=models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True) 

    def __str__(self):
        return str(self.nb_suite_parental)