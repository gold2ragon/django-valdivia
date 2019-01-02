from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    affair = forms.CharField(required=True)    
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), required=True)