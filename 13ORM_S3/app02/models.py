from django.db import models

# Create your models here.

class Role(models.Model):
    role_name = models.CharField(verbose_name='身份',max_length=12)
