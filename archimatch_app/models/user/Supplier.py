from django.db import models
from .ArchimatchUser import ArchimatchUser
from ..ArchiSubscription import ArchiSubscription
from django.core.exceptions import ValidationError
from ..utils.ArchitectType import ArchitectType
from archimatch_app.models.utils.BaseModel import BaseModel
from ..utils import ArchiServicetype,BankCard
from ..Preference import Preference

class Supplier(BaseModel):
    user = models.OneToOneField(ArchimatchUser, on_delete=models.CASCADE)
    
    
    
    supplier_avatar = models.ImageField(blank=True,null=True,upload_to='SupplierAvatars/')
    
    adress = models.CharField(max_length=255,default='',null=True)
    
    
    bio = models.TextField(max_length=1000,default='',null=True)
    company_name = models.CharField(max_length=255,default='',null=True)
    registration_number = models.CharField(max_length=255,default="",null=True)
    company_logo = models.ImageField(blank=True,null=True,upload_to='CompanyLogos/')
    first_cnx = models.BooleanField(default=False)
    video_presentation =  models.FileField(upload_to='ArchitectVideos/', blank=True, null=True)
    categories = models.CharField(max_length=255, null=True, blank=True,default='need1')
    chosen_spec = models.CharField(max_length=255, null=True, blank=True,default='')

    
    
    
    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name_plural = "Architects"
    
    
