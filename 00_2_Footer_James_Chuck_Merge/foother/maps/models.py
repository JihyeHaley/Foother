from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Review(models.Model):
    restaurant_address = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    restaurant_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)
    food_star = models.FloatField()
    food_review = models.CharField(max_length=300, default='nonono')
    food_image = ProcessedImageField(
                upload_to='upload_photo',
                processors=[ResizeToFill(200, 200)],
                format='JPEG',
                options={
                    'quality': 80}
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='')