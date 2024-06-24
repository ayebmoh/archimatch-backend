from archimatch_app.models.utils.BaseModel import BaseModel
from django.db import models
from django.core.exceptions import ValidationError



class Project(BaseModel): 
    architect_type = models.ForeignKey('archimatch_app.ArchitectType',on_delete=models.CASCADE, default=1)
    need = models.CharField(max_length=255, null=True, blank=True,default='need1')
    town = models.CharField(max_length=255, null=True, blank=True,default='need1')
    categories = models.CharField(max_length=255, null=True, blank=True,default='need1')  
    surface_terrain = models.CharField(max_length=255, null=True, blank=True,default='need1')
    surface_travaux = models.CharField(max_length=255, null=True, blank=True,default='need1')
    house_type = models.CharField(max_length=255, null=True, blank=True,default='need1') 
    work_type = models.CharField(max_length=255, null=True, blank=True,default='need1') 
    budget = models.CharField(max_length=255, null=True, blank=True,default='need1') 
    details = models.CharField(max_length=255, null=True, blank=True,default='need1') 
    work_style = models.CharField(max_length=255, null=True, blank=True,default='need1') 
    extra = models.CharField(max_length=255, null=True, blank=True,default='need1') 
    client = models.ForeignKey('archimatch_app.Client',on_delete=models.CASCADE,default=1)
    
    adresse  = models.CharField(max_length=255, blank=True, null=True,default='need1')
    need_pieces = models.OneToOneField('archimatch_app.NeedPieces',on_delete=models.CASCADE,default='1')

    
    def __str__(self):
        return self.adresse