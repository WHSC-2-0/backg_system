# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# 轮播图
class WhBanner(models.Model):
    img = models.CharField(max_length=255, verbose_name='图片', blank=True, null=True)
    time = models.CharField(max_length=32, verbose_name='上传时间', null=True, blank=True)
    jump_url = models.CharField(max_length=255, verbose_name='跳转路径', blank=True, null=True)

    class Meta:
        db_table = 'wh_banner'
