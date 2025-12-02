from django.db import models

# Create your models here.
class UserTb(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=12)
    phone = models.CharField(verbose_name='电话号码',max_length=11)
    gender = models.SmallIntegerField(verbose_name='性别',choices=((1,'男'),(0,'女')))

