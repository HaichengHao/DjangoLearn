from django.db import models

# Create your models here.

class Depart(models.Model):
    title = models.CharField(verbose_name='标题',max_length=32)
    class Meta:
        db_table = 'department'

class User(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=32)
    dp = models.ForeignKey(to='Depart',to_field='id',verbose_name='部门',on_delete=models.CASCADE)

class Role(models.Model):
    title = models.CharField(verbose_name='标题',max_length=32)


class Goods(models.Model):
    goods_name = models.CharField(verbose_name='商品名称',max_length=32)
    uid = models.ManyToManyField(to='User')


class Order(models.Model):
    gid = models.ForeignKey(to='Goods',to_field='id',verbose_name='商品id',on_delete=models.CASCADE)
    uid = models.ForeignKey(to='User',to_field='id',verbose_name='用户id',on_delete=models.CASCADE)