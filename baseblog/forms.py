from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField(required=True)
    to = forms.EmailField()
    subject = forms.CharField(required=True)
    comments = forms.CharField(widget=forms.Textarea, required=True)
