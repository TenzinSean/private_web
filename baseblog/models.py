from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
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
        return self.label


class PhotoCollection(models.Model):
    pass


class Contact(models.Model):
    pass

class StoryModel(models.Model):
    titre = models.CharField(max_length=255)
    sub_titre = models.CharField(max_length=30)
    context = models.TextField()
    pic = models.ImageField(upload_to = 'pic_folder/')

    def __str__(self):
        return self.titre


class Portofilo(models.Model):
    pass


class Projects(models.Model):
    pass
