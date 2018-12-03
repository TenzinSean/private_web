from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to = 'pic_folder/')


    def __str__(self):
        return self.title


class Travel(models.Model):
    label = models.CharField(max_length=255)
    content = models.TextField()
    pic = models.ImageField(upload_to = 'pic_folder/')

    def __str__(self):
        return self.title


class PhotoCollection(models.Model):
    pass


class StoryModel(models.Model):
    pass


class Portofilo(models.Model):
    pass


class Projects(models.Model):
    pass
