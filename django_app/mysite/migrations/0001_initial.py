# Generated by Django 2.1.5 on 2020-08-25 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesTaken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='履修科目名')),
                ('CT_status', models.IntegerField(choices=[(11, '日曜日'), (12, '月曜日'), (13, '火曜日'), (14, '水曜日'), (15, '木曜日'), (16, '金曜日'), (17, '土曜日')], verbose_name='曜日')),
                ('period', models.IntegerField(choices=[(1, '１限'), (2, '2限'), (3, '3限'), (4, '4限'), (5, '5限'), (6, '6限'), (7, '7限')], verbose_name='時限')),
                ('school_credit', models.IntegerField(default=0, verbose_name='単位数')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
