from datetime import datetime, date

from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16, db_index=True)
    age = models.IntegerField()
    pdate = models.DateField(verbose_name='注册日期', default=date.today)
    pdate_time = models.DateField(verbose_name='注册日期及时间', default=datetime.now)
    registe_date = models.DateField(verbose_name='注册时间', auto_now=True)
    salary = models.DecimalField(verbose_name='工资', max_digits=10, decimal_places=2,
                                 default=0.00)  # 总共十位数,有两位来保存小数,八位保存整数
    email = models.CharField(verbose_name='邮箱', unique=True, max_length=128, null=True,
                             blank=True)  # 一般开发中会指定邮箱为唯一邮箱,而用户名可以不唯一

    #新建一个字段显示用户的部门id,to表示关联的是哪张表!!!,to_field表示当前字段跟to的表的哪个字段关联
    did = models.ForeignKey(verbose_name="部门id",to='Department',to_field='id',on_delete=models.CASCADE)#important:其实to_field不写的话默认就会用to的表的id来作为外键,但是如果要用其它字段来连表的话就需要自己指定了


#
class Departement(models.Model):
    """部门表"""
    #由于django会默认帮我们生成id主键自增,所以我们不用自己设置,它会自动帮我们生成
    departement = models.CharField(verbose_name='部门',max_length=32)
