from django.db import models
from .BaseModel import BaseModel
from archimatch_app.models.user.ArchimatchUser import ArchimatchUser
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.utils import timezone


class Otp(BaseModel):
    user_id = models.ForeignKey(ArchimatchUser, related_name="otps", on_delete=models.CASCADE)
    code = models.IntegerField(validators=[
            MaxValueValidator(999999),  
            MinLengthValidator(6),
        ])
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.code)

    def is_expired(self):
        expiration_time = self.creation_time + timezone.timedelta(minutes=2)
        return timezone.now() > expiration_time

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set creation time if the object is being newly created
            self.creation_time = timezone.now()
        super().save(*args, **kwargs)

    def delete_if_expired(self):
        if self.is_expired():
            self.delete()