from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.URLField
    prompt = models.TextField
    