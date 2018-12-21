from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView
from .models import Blog, Travel, StoryModel
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError # email set up
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
class HomePage(ListView):
    model = Blog
    template_name = 'second.html'


class StoryPage(ListView):
    model = StoryModel
    template_name = 'story.html'


class Portfilo(TemplateView):
    template_name = 'portfilo.html'


class Projects(TemplateView):
    template_name = 'projects.html'


class Travel(ListView):
    model = Travel
    template_name = "travel.html"


class Contact(TemplateView):
    template_name = 'contact.html'



def emailView(request):
    sent = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = '{} ({}) recommends you reading: saying {}'.format(cd['name'],
            cd['email'], cd['subject'])
            message = 'Read {} comments:{}:'.format(cd['name'],cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'sent': sent})


def successView(request):
    return HttpResponse('Success! Thank you for you messagae')

class LogIn(TemplateView):
    template_name = 'login.html'
