# Generated by Django 2.1.15 on 2020-06-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200628_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_score',
            field=models.IntegerField(default=0),
        ),
    ]
