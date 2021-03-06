# Generated by Django 2.1.15 on 2020-06-29 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_address', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('restaurant_name', models.CharField(max_length=100)),
                ('food_name', models.CharField(max_length=100)),
                ('food_star', models.FloatField()),
                ('food_image', imagekit.models.fields.ProcessedImageField(upload_to='upload_photo')),
                ('upload_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_upload', models.ManyToManyField(related_name='user_upload', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
