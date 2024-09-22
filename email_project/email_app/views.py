from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from .forms import EmailForm

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, sender, [recipient])
            return render(request, 'success.html')
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})
    # return HttpResponse('hello sukhchain singh')
