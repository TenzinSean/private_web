from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')


    def __str__(self):
        return self.title
