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
    name = models.CharField(max_length=100, verbose_name='广告名字', blank=True, null=True)
    is_show = models.SmallIntegerField(verbose_name='是否显示', blank=True, null=True)
    place_id = models.IntegerField(verbose_name='广告位置', blank=True,null=True)

    class Meta:
        db_table = 'wh_banner'


class WhBanPlace(models.Model):
    name = models.CharField(max_length=255, verbose_name='广告名称', blank=True, null=True)
    wight = models.IntegerField(verbose_name='广告宽度', blank=True, null=True)
    height = models.IntegerField(verbose_name='广告高度', blank=True, null=True)
    desc = models.CharField(max_length=255, verbose_name='广告描述', blank=True, null=True)
    status = models.SmallIntegerField(verbose_name='广告状态', blank=True, null=True)

    class Meta:
        db_table = 'wh_ban_place'
