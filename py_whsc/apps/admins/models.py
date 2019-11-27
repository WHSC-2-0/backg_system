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


class SyAdmin(models.Model):
    admin_id = models.PositiveSmallIntegerField(primary_key=True)
    admin_name = models.CharField(max_length=60)
    admin_pwd = models.CharField(max_length=32)
    add_time = models.IntegerField()
    last_login = models.IntegerField()
    last_ip = models.CharField(max_length=15)
    role_id = models.SmallIntegerField(blank=True, null=True)
    pwd2 = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_admin'


class SyAdminRole(models.Model):
    role_id = models.PositiveSmallIntegerField(primary_key=True)
    role_name = models.CharField(max_length=30, blank=True, null=True)
    act_list = models.TextField(blank=True, null=True)
    role_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_admin_role'


class SySystemMenu(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    group = models.CharField(max_length=20, blank=True, null=True)
    right = models.TextField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_system_menu'
