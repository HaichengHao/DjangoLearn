from django.db import models
# Create your models here.

class Goods(models.Model):
    goods_name = models.CharField(verbose_name='商品名称',max_length=16)
    goods_price = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)


#tips:创建goods_user表来进行多对多表构建
class Goods_User(models.Model):
    user_id = models.ForeignKey(to="user.User",to_field="id",on_delete=models.CASCADE)
    goods_id = models.ForeignKey(to="Goods",to_field="id",on_delete=models.CASCADE)
