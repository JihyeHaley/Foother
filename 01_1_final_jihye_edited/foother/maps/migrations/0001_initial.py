# Generated by Django 2.1.15 on 2020-07-25 10:29

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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('restaurant_address', models.CharField(max_length=30)),
                ('restaurant_name', models.CharField(max_length=30)),
                ('food_name', models.CharField(max_length=30)),
                ('food_review', models.CharField(max_length=30)),
                ('food_star', models.IntegerField()),
                ('food_image', imagekit.models.fields.ProcessedImageField(upload_to='upload_photo')),
                ('visit_date', models.DateField()),
                ('food_kind', models.CharField(max_length=10)),
                ('like_users', models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='which_review', to='maps.Review'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='which_user', to=settings.AUTH_USER_MODEL),
        ),
    ]