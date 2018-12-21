from django.urls import path
from django.views.generic.base import TemplateView

from .views import (
                HomePage,
                StoryPage,
                Portfilo,
                Projects,
                Travel,
                Contact,
                LogIn,
                emailView,
                successView
                )

from . import views

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('story/', StoryPage.as_view(), name='story'),
    path('portfilo/', Portfilo.as_view(), name='portfilo'),
    path('projects/', Projects.as_view(), name='projects'),
    path('travel/', Travel.as_view(), name='travel'),
    path('Contact/', emailView, name='contacts'),
    path('success/', successView, name='success'),
    path('Login/', LogIn.as_view(), name='login'),
    path('loginone/', TemplateView.as_view(template_name='home.html')),
]
