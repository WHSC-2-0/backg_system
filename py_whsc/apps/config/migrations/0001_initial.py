# Generated by Django 2.2.3 on 2019-12-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(blank=True, max_length=255, null=True, verbose_name='图片')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='上传时间')),
                ('jump_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='跳转路径')),
            ],
            options={
                'db_table': 'wh_banner',
            },
        ),
    ]
