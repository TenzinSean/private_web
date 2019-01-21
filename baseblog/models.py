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


class Pola(models.Model):
    chaptre = models.CharField(max_length=255) # title
    title_chap = models.CharField(max_length=255)
    contenu = models.TextField()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'likes', blank=True)
    pic_one = models.ImageField(upload_to = 'pic_folder/')

    def __str__(self):
        return self.chaptre

# comments


class Family(models.Model):
    chaptre1 = models.CharField(max_length=255)
    title_chap1 = models.CharField(max_length=255)
    contenu1 = models.TextField()
    pic_two = models.ImageField(upload_to = 'pic_folder/')

    def __str__(self):
        return self.chaptre1

class Portofilo(models.Model):
    pass


class Projects(models.Model):
    pass

# Comments are here
class Comment(models.Model):
    post = models.ForeignKey(Pola,
                            on_delete=models.CASCADE,
                            related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
