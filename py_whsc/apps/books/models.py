# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# 小说一级分类模型
class WhTypeOne(models.Model):
    tap_name = models.CharField(max_length=100, verbose_name='一级分类名称', blank=True, null=True)

    class Meta:
        db_table = 'wh_type_one'


# 小说分类二级模型
class WhTypeChild(models.Model):
    t = models.ForeignKey(WhTypeOne, on_delete=models.CASCADE, verbose_name='一级分类id', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='二级分类名称', blank=True, null=True)

    class Meta:
        db_table = 'wh_type_child'


# 小说模型
class WhBook(models.Model):
    c = models.ForeignKey(WhTypeChild, on_delete=models.CASCADE, verbose_name='关联二级分类', blank=True, null=True)
    b_name = models.CharField(max_length=100, verbose_name='书名', blank=True, null=True)
    b_img = models.CharField(max_length=255, verbose_name='封面图片', blank=True, null=True)
    b_desc = models.CharField(max_length=255, verbose_name='描述', blank=True, null=True)
    b_auhtor = models.CharField(max_length=100, verbose_name='作者', blank=True, null=True)
    b_content_url = models.CharField(max_length=100, verbose_name='内容地址', blank=True, null=True)
    add_time = models.CharField(max_length=32, verbose_name='上传时间', blank=True, null=True)
    read_num = models.IntegerField(verbose_name='阅读量', blank=True, null=True)
    new_chapter = models.CharField(max_length=50, verbose_name='最新章节', blank=True, null=True)

    class Meta:
        db_table = 'wh_book'


# 目录模型
class WhCatalog(models.Model):
    book = models.ForeignKey(WhBook, on_delete=models.CASCADE, verbose_name='关联小说', blank=True, null=True)
    c_name = models.CharField(max_length=50, verbose_name='章节名称', blank=True, null=True)
    add_time = models.CharField(max_length=32, verbose_name='添加时间', blank=True, null=True)

    class Meta:
        db_table = 'wh_catalog'


class WhNotice(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'wh_notice'


class WhReadlog(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID')
    book_id = models.IntegerField(verbose_name='小说ID')

    class Meta:
        db_table = 'wh_readlog'
