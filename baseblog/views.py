from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Blog


# Create your views here.
class HomePage(ListView):
    model = Blog
    template_name = 'second.html'


class StoryPage(TemplateView):
    template_name = 'story.html'


class Portfilo(TemplateView):
    template_name = 'portfilo.html'


class Projects(TemplateView):
    template_name = 'projects.html'


class Contact(TemplateView):
    template_name = 'contact.html'
