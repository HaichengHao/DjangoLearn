from django.db import models

# Create your models here.


#创建一个文章表
class Articles(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    detail = models.TextField(blank=True,null=True) #textfield存储的信息要比charfield要多很多