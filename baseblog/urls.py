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
                successView,
                PolaStory,
                FamilyStory,
                ChaptreChab1,
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
    #path('Login/', LogIn.as_view(), name='login'),
    path('secret/', views.secret_page, name='secret'),
    path('pola/', PolaStory.as_view(), name='pola'),
    #path('PolaChap1/', Chaptre1.as_view(), name="polaChap1"),
    path('PolaChap1/', views.post_detail, name='polaChap1'),
    path('family/', FamilyStory.as_view(), name='family'),
    path('familyChap1/', ChaptreChab1.as_view(), name="chabChap1"),
    path('like/', views.like_post, name='like_post'),
]
