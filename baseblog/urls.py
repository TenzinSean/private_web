from django.urls import path

from .views import HomePage, StoryPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('story/', StoryPage.as_view(), name='story'),
]
