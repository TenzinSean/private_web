from django import forms
from .models import Comment

class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField(required=True)
    to = forms.EmailField()
    subject = forms.CharField(required=True)
    comments = forms.CharField(widget=forms.Textarea, required=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
