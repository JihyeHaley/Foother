from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    user_phone = models.CharField(max_length=13)
    user_birth = models.DateField(auto_now_add=False, default='20200321')
    user_created = models.DateTimeField(auto_now_add=True)
    user_score = models.IntegerField(default=0)
    user_profile_image = ProcessedImageField(
                    upload_to = 'user_profile_image',
                    processors=[ResizeToFill(500, 500)],
                    format='JPEG',
                    options={
                        'quality': 70},
                    default='default.png'
    )
    # class Meta:
    #     ordering = ['-score']
    