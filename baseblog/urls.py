from django.urls import path

from .views import (
                HomePage,
                StoryPage,
                Portfilo,
                Projects,
                Contact)


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('story/', StoryPage.as_view(), name='story'),
    path('portfilo/', Portfilo.as_view(), name='portfilo'),
    path('projects/', Projects.as_view(), name='projects'),
    path('Contact/', Contact.as_view(), name='contacts')
]
