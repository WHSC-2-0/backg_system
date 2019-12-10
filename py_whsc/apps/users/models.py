# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# 用户模型
class WhUsers(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    paypwd = models.CharField(max_length=50, blank=True, null=True)
    reg_time = models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    head_pic = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    is_lock = models.SmallIntegerField(blank=True, null=True)
    tjr_id = models.IntegerField(blank=True, null=True)
    totalnum = models.IntegerField(blank=True, null=True)
    ztnum = models.IntegerField(blank=True, null=True)
    idcard = models.CharField(max_length=50, blank=True, null=True)
    is_shiming = models.SmallIntegerField(blank=True, null=True)
    realname = models.CharField(max_length=50, blank=True, null=True)
    self_htlv = models.FloatField(blank=True, null=True)
    total_htlv = models.FloatField(blank=True, null=True)
    big_htlv = models.FloatField(blank=True, null=True)
    small_htlv = models.FloatField(blank=True, null=True)
    is_shiming_zs = models.SmallIntegerField(blank=True, null=True)
    qr_code = models.CharField(max_length=255, blank=True, null=True)
    first_read = models.DateTimeField(blank=True, null=True)
    tmp_read = models.DateTimeField(blank=True, null=True)
    appid = models.CharField(max_length=100, blank=True, null=True)
    user_key = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wh_users'


# 实名订单模型
class WhCertification(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('WhUsers', models.DO_NOTHING, blank=True, null=True)
    p_money = models.FloatField(blank=True, null=True)
    order_num = models.CharField(max_length=50, blank=True, null=True)
    set_time = models.DateTimeField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wh_certification'


# 交易明细模型
class WhDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('WhUsers', models.DO_NOTHING, blank=True, null=True)
    money = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wh_detail'


# 短信模型
class WhMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('WhUsers', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    msg = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wh_message'


# 支付订单模型
class WhPayOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('WhUsers', models.DO_NOTHING, blank=True, null=True)
    money = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    order_num = models.CharField(max_length=100, blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wh_pay_order'


# 钱包模型
class WhWallet(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(WhUsers, models.DO_NOTHING, blank=True, null=True)
    money = models.FloatField(blank=True, null=True)
    wechat = models.CharField(max_length=255, blank=True, null=True)
    alipay = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wh_wallet'
