from django.shortcuts import render


def email_template(request):
    text ="Hello world"
    context = {
        'context_text' : text
    }
    return render(request,'welcome_email.html',context)