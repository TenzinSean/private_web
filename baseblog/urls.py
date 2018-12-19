from django.urls import path

from .views import (
                HomePage,
                StoryPage,
                Portfilo,
                Projects,
                Travel,
                Contact,
                LogIn,
                )

from . import views


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('story/', StoryPage.as_view(), name='story'),
    path('portfilo/', Portfilo.as_view(), name='portfilo'),
    path('projects/', Projects.as_view(), name='projects'),
    path('travel/', Travel.as_view(), name='travel'),
    path('Contact/', Contact.as_view(), name='contacts'),
    path('Login/', LogIn.as_view(), name='login'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),

]
