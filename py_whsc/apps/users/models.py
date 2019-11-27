# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class SyUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=32)
    paypwd = models.CharField(max_length=32, blank=True, null=True)
    address_id = models.PositiveIntegerField()
    reg_time = models.PositiveIntegerField()
    last_login = models.PositiveIntegerField()
    last_ip = models.CharField(max_length=15)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    head_pic = models.CharField(max_length=255, blank=True, null=True)
    qq = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    mobile = models.CharField(max_length=20)
    oauth = models.CharField(max_length=10, blank=True, null=True)
    openid = models.CharField(max_length=100, blank=True, null=True)
    unionid = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    is_lock = models.IntegerField(blank=True, null=True)
    tjstr = models.TextField(blank=True, null=True)
    bank_card = models.CharField(max_length=100, blank=True, null=True)
    bank_huming = models.CharField(max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    weixin = models.CharField(max_length=100, blank=True, null=True)
    zhifubao = models.CharField(max_length=100, blank=True, null=True)
    tjr_id = models.IntegerField()
    tjr_name = models.CharField(max_length=50)
    depth = models.IntegerField()
    totalnum = models.IntegerField(blank=True, null=True)
    tjnum = models.IntegerField(blank=True, null=True)
    gl_id = models.IntegerField(blank=True, null=True)
    glstr = models.TextField(blank=True, null=True)
    is_bd = models.IntegerField(blank=True, null=True)
    gl_name = models.CharField(max_length=50, blank=True, null=True)
    pos = models.IntegerField(blank=True, null=True)
    bdusername = models.CharField(max_length=50, blank=True, null=True)
    posnum = models.IntegerField(blank=True, null=True)
    gldepth = models.IntegerField(blank=True, null=True)
    tjvipnum = models.IntegerField(blank=True, null=True)
    tjjifen = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bdnum = models.IntegerField(blank=True, null=True)
    bdprice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sylevel = models.IntegerField(blank=True, null=True)
    salenum = models.IntegerField(blank=True, null=True)
    cfnum = models.IntegerField(blank=True, null=True)
    sy_1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sy_2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zhu_username = models.CharField(max_length=50, blank=True, null=True)
    ischild = models.IntegerField(blank=True, null=True)
    erweima = models.CharField(max_length=255, blank=True, null=True)
    set_cfnum = models.IntegerField(blank=True, null=True)
    ywsalenum = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    level1 = models.IntegerField(blank=True, null=True)
    idcard = models.CharField(max_length=30, blank=True, null=True)
    total_htlv = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    is_shiming = models.IntegerField(blank=True, null=True)
    small_htlv = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    appid = models.CharField(max_length=50, blank=True, null=True)
    first_read = models.IntegerField(blank=True, null=True)
    tmp_read = models.IntegerField(blank=True, null=True)
    team_quittime = models.IntegerField(blank=True, null=True)
    realname = models.CharField(max_length=50, blank=True, null=True)
    is_shiming_zs = models.IntegerField(blank=True, null=True)
    woleid = models.CharField(max_length=255, blank=True, null=True)
    numsb = models.IntegerField()
    dj_reason = models.CharField(max_length=255, blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    rzfee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_users'
