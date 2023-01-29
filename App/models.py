from django.db import models
from datetime import datetime

# Create your models here.


class Metiers(models.Model):
    metiers_id = models.IntegerField()
    metiers_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    metiers_description = models.TextField()
    metiers_image = models.ImageField(upload_to='images/%y/%m/%d',
                                      verbose_name='images', default="images/22/11/24/images.png")
    metiers_image2 = models.ImageField(upload_to='images2/%y/%m/%d',
                                       verbose_name='images2', default="images2/22/11/24/images2.png")
    Created = models.DateTimeField(default=datetime.now)
    metiers_detaille = models.TextField()

    def __str__(self):
        return self.metiers_name
