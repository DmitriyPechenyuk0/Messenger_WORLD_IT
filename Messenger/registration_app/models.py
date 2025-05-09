from django.db import models

# Create your models here.

class RegistrationCodes(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)

