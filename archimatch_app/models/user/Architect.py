from django.db import models
from .ArchimatchUser import ArchimatchUser
from ..ArchiSubscription import ArchiSubscription
from django.core.exceptions import ValidationError
from ..utils.ArchitectType import ArchitectType
from archimatch_app.models.utils.BaseModel import BaseModel
from ..utils import ArchiServicetype,BankCard
from ..Preference import Preference

class Architect(BaseModel):
    user = models.OneToOneField(ArchimatchUser, on_delete=models.CASCADE)
    tokens = models.IntegerField(default=5)
    verified = models.BooleanField(default=False)
    shared = models.BooleanField(default=False)
    architect_avatar = models.ImageField(blank=True,null=True,upload_to='ArchitectsAvatars/')
    services = models.ManyToManyField(ArchiServicetype, related_name='architects')
    adress = models.CharField(max_length=255,default='',null=True)
    arch_identifier = models.CharField(max_length=10,default='',null=True)
    arch_type = models.ForeignKey(ArchitectType, related_name='architects', on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000,default='',null=True)
    company_name = models.CharField(max_length=255,default='',null=True)
    registration_number = models.CharField(max_length=255,default="",null=True)
    company_logo = models.ImageField(blank=True,null=True,upload_to='CompanyLogos/')
    first_cnx = models.BooleanField(default=False)
    video_presentation =  models.FileField(upload_to='ArchitectVideos/', blank=True, null=True)
    categories = models.CharField(max_length=255, null=True, blank=True,default='need1')
    house_type = models.CharField(max_length=255, null=True, blank=True,default='need1') 
    work_type = models.CharField(max_length=255, null=True, blank=True,default='need1')
    work_style = models.CharField(max_length=255, null=True, blank=True,default='need1')
    complexity = models.CharField(max_length=255, null=True, blank=True,default='need1')
    subscription = models.OneToOneField(ArchiSubscription,on_delete=models.SET_NULL,null=True, default=None)
    bankcard = models.OneToOneField(BankCard, on_delete=models.SET_NULL,null=True, default=None)
    preference = models.OneToOneField(Preference, on_delete=models.SET_NULL,null=True, default=None)
    
    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name_plural = "Architects"
    
    
