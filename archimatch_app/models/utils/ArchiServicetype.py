from django.db import models

class ArchiServicetype(models.Model):
    display = models.CharField(max_length=255)
    def __str__(self):
        return self.display