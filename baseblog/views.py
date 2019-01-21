from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, CreateView
from .models import Blog, Travel, StoryModel, Pola, Family, Comment
from .forms import ContactForm, CommentForm
from django.core.mail import send_mail, BadHeaderError # email set up
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

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

# Contact form
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
#Authentication
class LogIn(TemplateView):
    template_name = 'login.html'

#Pola
class PolaStory(ListView):
    model = Pola
    template_name ='Pola/chaptre1.html'


class Chaptre1(ListView):
    model = Pola
    template_name = 'Pola/Detail/chaptreFull.html'




# the issue with comment system with view points

def post_detail(request, year, month, day, post):
    #post = get_object_or_404(Pola, slug=post, status='published',publish__year=year, publish__month=month, publish__day=day)
    post = Pola.objects.all()
     #list of active Comments
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                 'Pola/Detail/chaptreFull.html',
                 {'post': post,
                 'comments': comments,
                 'new_comment': new_comment,
                 'comment_form': comment_form})


#Chabdeltsang
class FamilyStory(ListView):
    model = Family
    template_name = 'Chabdeltsang/chaptre.html'

# Chaptre1
class ChaptreChab1(ListView):
    model = Family
    template_name = 'Chabdeltsang/Detail/chaptreFull.html'

def like_post(request):
    post = get_object_or_404(Pola, id=float(request.POST.get('post_id')))
    post.likes.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())


# Protected views
@login_required
def secret_page(request):
    return render(request, 'secret_page.html')
