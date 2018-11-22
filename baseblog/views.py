from django.shortcuts import render
from django.views.generic import ListView, TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name = 'second.html'


class StoryPage(TemplateView):
    template_name = 'story.html'
