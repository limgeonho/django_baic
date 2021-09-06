from django.shortcuts import render
from .forms import MailForm


def ping(request):
    # form 보내주기
    form = MailForm() # HTML
    context = {
        'form': form
    }
    return render(request, 'newsletter/ping.html', context)

def pong(request):
    form = MailForm(request.POST) # Validation(+ HTML) : 아직 유효성 검사 전임!!
    if form.is_valid():
        pass
    