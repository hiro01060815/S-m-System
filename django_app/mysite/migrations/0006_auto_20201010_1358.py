# Generated by Django 3.1 on 2020-10-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20200928_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='kadaiinfo',
            name='submit_date',
            field=models.DateTimeField(null=True, verbose_name='提出した日'),
        ),
        migrations.AlterField(
            model_name='kadaiinfo',
            name='date',
            field=models.DateTimeField(default='2020-10-08 12:00', verbose_name='提出期日'),
        ),
    ]
