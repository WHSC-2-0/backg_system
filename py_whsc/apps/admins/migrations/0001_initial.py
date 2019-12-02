# Generated by Django 2.2.7 on 2019-12-01 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhAdmin',
            fields=[
                ('admin_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='管理员id')),
                ('admin_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='管理员名称')),
                ('admin_mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号')),
                ('login_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='管理员账号')),
                ('login_pwd', models.CharField(blank=True, max_length=32, null=True, verbose_name='管理员密码')),
                ('login_pwd1', models.CharField(blank=True, max_length=32, null=True, verbose_name='确认管理员密码')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('last_login_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='上次登录时间')),
                ('login_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登录时间')),
                ('last_ip', models.CharField(blank=True, max_length=15, null=True, verbose_name='上次登录ip')),
                ('pwd2', models.CharField(blank=True, max_length=32, null=True, verbose_name='二级密码')),
            ],
            options={
                'db_table': 'wh_admin',
            },
        ),
        migrations.CreateModel(
            name='WhAdminGroup',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False, verbose_name='分组ID')),
                ('parent_group_id', models.IntegerField(blank=True, null=True, verbose_name='父级分组ID')),
                ('group_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='分组名称')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='分组描述')),
            ],
            options={
                'db_table': 'wh_admin_group',
            },
        ),
        migrations.CreateModel(
            name='WhAdminRight',
            fields=[
                ('right_id', models.AutoField(primary_key=True, serialize=False, verbose_name='权限ID')),
                ('parent_right_id', models.IntegerField(blank=True, null=True, verbose_name='父级权限ID')),
                ('right_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='权限名称')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='权限描述')),
            ],
            options={
                'db_table': 'wh_admin_right',
            },
        ),
        migrations.CreateModel(
            name='WhAdminRole',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False, verbose_name='角色ID')),
                ('parent_role_id', models.IntegerField(blank=True, null=True, verbose_name='父级角色ID')),
                ('role_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='角色名称')),
                ('add_time', models.IntegerField(verbose_name='添加时间')),
                ('description', models.CharField(max_length=200, verbose_name='角色描述')),
            ],
            options={
                'db_table': 'wh_admin_role',
            },
        ),
        migrations.CreateModel(
            name='WhOrganization',
            fields=[
                ('o_id', models.AutoField(primary_key=True, serialize=False, verbose_name='组织ID')),
                ('parent_o_id', models.IntegerField(verbose_name='父级组织ID')),
                ('o_name', models.CharField(max_length=64, verbose_name='组织名称')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='组织描述')),
                ('right_type', models.PositiveSmallIntegerField(choices=[('0', '可访问'), ('1', '可操作')], default=0, verbose_name='权限类型')),
            ],
            options={
                'db_table': 'wh_organization',
            },
        ),
        migrations.CreateModel(
            name='WhRoleRightRelation',
            fields=[
                ('rrr_id', models.AutoField(primary_key=True, serialize=False, verbose_name='角色权限ID')),
                ('right_type', models.PositiveSmallIntegerField(choices=[('0', '可访问'), ('1', '可操作')], default=0, verbose_name='权限类型')),
                ('right', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdminRight', verbose_name='权限ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdminRole', verbose_name='角色ID')),
            ],
            options={
                'db_table': 'wh_role_right',
            },
        ),
        migrations.CreateModel(
            name='WhGroupRoleRelation',
            fields=[
                ('grr_id', models.AutoField(primary_key=True, serialize=False, verbose_name='组角色ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdminGroup', verbose_name='分组ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdminRole', verbose_name='角色ID')),
            ],
            options={
                'db_table': 'wh_group_role',
            },
        ),
        migrations.CreateModel(
            name='WhGroupRightRelation',
            fields=[
                ('grr_id', models.AutoField(primary_key=True, serialize=False, verbose_name='分组权限ID')),
                ('right_type', models.PositiveSmallIntegerField(choices=[('0', '可访问'), ('1', '可操作')], default=0, verbose_name='权限类型')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdminGroup', verbose_name='分组ID')),
                ('right', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdminRight', verbose_name='权限ID')),
            ],
            options={
                'db_table': 'wh_group_right',
            },
        ),
        migrations.CreateModel(
            name='WhAdminRoleRelation',
            fields=[
                ('grr_id', models.AutoField(primary_key=True, serialize=False, verbose_name='管理员角色ID')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdmin', verbose_name='管理员ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdminRole', verbose_name='角色ID')),
            ],
            options={
                'db_table': 'wh_admin_role_relation',
            },
        ),
        migrations.CreateModel(
            name='WhAdminLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False, verbose_name='日志ID')),
                ('op_type', models.IntegerField(verbose_name='操作类型')),
                ('o_name', models.CharField(max_length=200, verbose_name='操作内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('o_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdmin', verbose_name='操作人')),
            ],
            options={
                'db_table': 'wh_admin_log',
            },
        ),
        migrations.CreateModel(
            name='WhAdminGroupRelation',
            fields=[
                ('grr_id', models.AutoField(primary_key=True, serialize=False, verbose_name='管理员分组ID')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdmin', verbose_name='管理员ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdminGroup', verbose_name='分组ID')),
            ],
            options={
                'db_table': 'wh_admin_group_relation',
            },
        ),
        migrations.AddField(
            model_name='whadmin',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.WhAdminGroup', verbose_name='所属组织'),
        ),
    ]
