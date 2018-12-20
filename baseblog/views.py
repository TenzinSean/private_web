from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Blog, Travel, StoryModel
from .forms import EmailPostForm
from django.core.mail import send_mail # email set up


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


def post_share(request, post_id):
    post = get_object_or_404(Contact, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # From was submit
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading " {}"'.format(cd['name'],
            cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'],cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'contact.html', {'post': post, 'form': form, 'sent': sent})



class LogIn(TemplateView):
    template_name = 'login.html'
