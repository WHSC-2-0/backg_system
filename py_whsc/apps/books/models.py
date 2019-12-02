# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'table'
# The error was: (1146, "Table 'hfgdsfwsdsaf.table' doesn't exist")


class SyBook(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(verbose_name='Img', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(verbose_name='Author', max_length=100, blank=True, null=True)  # Field name made lowercase.
    desc = models.TextField(verbose_name='Desc', blank=True, null=True)  # Field name made lowercase.
    cid = models.IntegerField(verbose_name='CId', blank=True, null=True)  # Field name made lowercase.
    cname = models.CharField(verbose_name='CName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bookstatus = models.CharField(verbose_name='BookStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    add_time = models.IntegerField(blank=True, null=True)
    score = models.DecimalField(verbose_name='Score', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(blank=True, null=True)
    renqi = models.IntegerField(verbose_name='Renqi', blank=True, null=True)  # Field name made lowercase.
    week = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    lasttime = models.IntegerField(verbose_name='LastTime', blank=True, null=True)  # Field name made lowercase.
    is_show = models.PositiveIntegerField()
    lastchapterid = models.IntegerField(verbose_name='LastChapterId', blank=True, null=True)  # Field name made lowercase.
    lastchapter = models.CharField(verbose_name='LastChapter', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(blank=True, null=True)
    sytype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_book'

