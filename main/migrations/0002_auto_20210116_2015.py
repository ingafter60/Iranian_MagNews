# Generated by Django 2.2.5 on 2021-01-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='pin',
            field=models.CharField(default='Null', max_length=40),
        ),
        migrations.AddField(
            model_name='main',
            name='vi',
            field=models.CharField(default='Null', max_length=40),
        ),
        migrations.AlterField(
            model_name='main',
            name='about',
            field=models.TextField(default=''),
        ),
    ]
