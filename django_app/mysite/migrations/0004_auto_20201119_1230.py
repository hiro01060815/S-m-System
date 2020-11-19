# Generated by Django 3.1 on 2020-11-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20201117_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='baitotimeinfo',
            name='holiday',
            field=models.IntegerField(choices=[(0, '平日'), (1, '日祝')], default=0, verbose_name='平日or日祝'),
        ),
        migrations.AlterField(
            model_name='baitotimeinfo',
            name='in_time',
            field=models.DateTimeField(default='2020-11-19 12:30', verbose_name='出勤時間'),
        ),
        migrations.AlterField(
            model_name='baitotimeinfo',
            name='out_time',
            field=models.DateTimeField(default='2020-11-19 12:30', verbose_name='退勤時間'),
        ),
        migrations.AlterField(
            model_name='kadaiinfo',
            name='date',
            field=models.DateTimeField(default='2020-11-19 12:30', verbose_name='提出期日'),
        ),
    ]