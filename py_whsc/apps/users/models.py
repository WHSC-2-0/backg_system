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
    user_name = models.CharField(max_length=50, verbose_name='用户名', blank=True, null=True)
    password = models.CharField(max_length=50, verbose_name='登录密码', blank=True, null=True)
    paypwd = models.CharField(max_length=50, verbose_name='支付密码', blank=True, null=True)
    reg_time = models.DateTimeField(verbose_name='注册时间', blank=True, null=True)
    last_ip = models.CharField(max_length=50, verbose_name='登录ip', blank=True, null=True)
    nickname = models.CharField(max_length=255, verbose_name='昵称', blank=True, null=True)
    head_pic = models.CharField(max_length=255, verbose_name='头像', blank=True, null=True)
    phone = models.IntegerField(verbose_name='手机号', blank=True, null=True)
    is_lock = models.SmallIntegerField(verbose_name='是否锁定', blank=True, null=True)
    tjr_id = models.IntegerField(verbose_name='推荐人id', blank=True, null=True)
    totalnum = models.IntegerField(verbose_name='团队人数', blank=True, null=True)
    ztnum = models.IntegerField(verbose_name='直推人数', blank=True, null=True)
    idcard = models.CharField(verbose_name='身份证号', max_length=50, blank=True, null=True)
    is_shiming = models.SmallIntegerField(verbose_name='是否实名', blank=True, null=True)
    realname = models.CharField(max_length=50, verbose_name='实名姓名', blank=True, null=True)
    self_htlv = models.FloatField(verbose_name='个人回头率', blank=True, null=True)
    total_htlv = models.FloatField(verbose_name='团队回头率', blank=True, null=True)
    big_htlv = models.FloatField(verbose_name='大区回头率', blank=True, null=True)
    small_htlv = models.FloatField(verbose_name='小区回头率', blank=True, null=True)
    is_shiming_zs = models.SmallIntegerField(verbose_name='是否实名赠送', blank=True, null=True)
    qr_code = models.CharField(max_length=255, verbose_name='推广二维码', blank=True, null=True)
    first_read = models.DateTimeField(verbose_name='今日首次阅读时间', blank=True, null=True)
    tmp_read = models.DateTimeField(verbose_name='今日完成阅读时间', blank=True, null=True)
    appid = models.CharField(max_length=100, verbose_name='设备号（不可修改）', blank=True, null=True)
    user_key = models.CharField(max_length=100, verbose_name='连接密匙', blank=True, null=True)

    class Meta:
        db_table = 'wh_users'


# 实名订单模型
class WhCertification(models.Model):
    user = models.ForeignKey(WhUsers, on_delete=models.CASCADE, verbose_name='关联用户', blank=True, null=True)
    p_money = models.FloatField(verbose_name='支付金额', blank=True, null=True)
    order_num = models.CharField(max_length=50, verbose_name='订单号', blank=True, null=True)
    set_time = models.DateTimeField(verbose_name='创建时间', blank=True, null=True)
    pay_time = models.DateTimeField(verbose_name='支付时间', blank=True, null=True)
    status = models.SmallIntegerField(verbose_name='支付状态', default=0, blank=True, null=True)

    class Meta:
        db_table = 'wh_certification'


# 交易明细模型
class WhDetail(models.Model):
    user = models.ForeignKey(WhUsers, on_delete=models.CASCADE, verbose_name='关联用户', blank=True, null=True)
    money = models.FloatField(verbose_name='交易金额', blank=True, null=True)
    status = models.SmallIntegerField(verbose_name='状态', blank=True, null=True)
    time = models.DateTimeField(verbose_name='交易时间', blank=True, null=True)

    class Meta:
        db_table = 'wh_detail'


# 短信模型
class WhMessage(models.Model):
    user = models.ForeignKey(WhUsers, on_delete=models.CASCADE, verbose_name='关联用户', blank=True, null=True)
    """发送状态（0:未发送，1：已成功，2：未成功）"""
    status = models.SmallIntegerField(verbose_name='发送状态', default=0, blank=True, null=True)
    send_time = models.DateTimeField(verbose_name='发送时间', blank=True, null=True)
    msg = models.CharField(max_length=255, verbose_name='内容', blank=True, null=True)

    class Meta:
        db_table = 'wh_message'


# 支付订单模型
class WhPayOrder(models.Model):
    user = models.ForeignKey(WhUsers, on_delete=models.CASCADE, verbose_name='关联用户', blank=True, null=True)
    money = models.FloatField(verbose_name='支付金额', blank=True, null=True)
    type = models.CharField(max_length=50, verbose_name='支付类型', blank=True, null=True)
    order_num = models.CharField(max_length=100, verbose_name='订单号', blank=True, null=True)
    pay_time = models.DateTimeField(verbose_name='支付时间', blank=True, null=True)
    """支付状态（0：未支付，1：已支付）"""
    status = models.SmallIntegerField(verbose_name='支付状态', default=0, blank=True, null=True)

    class Meta:
        db_table = 'wh_pay_order'


# 钱包模型
class WhWallet(models.Model):
    user = models.ForeignKey(WhUsers, on_delete=models.CASCADE, verbose_name='关联用户', blank=True, null=True)
    money = models.FloatField(verbose_name='余额（￥）', blank=True, null=True)
    wechat = models.CharField(verbose_name='微信', max_length=255, blank=True, null=True)
    alipay = models.CharField(verbose_name='支付宝', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'wh_wallet'
