# Generated by Django 2.2.4 on 2019-08-03 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rainforest', '0006_auto_20190803_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewer',
        ),
    ]
