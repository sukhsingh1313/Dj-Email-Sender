from django import forms

class EmailForm(forms.Form):
    sender = forms.EmailField(label='Email_default sender')
    recipient = forms.EmailField(label='Recipient Email')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
