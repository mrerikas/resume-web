from django.shortcuts import render

# from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, "home.html", {})


def success(request):
    return render(request, "success.html", {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_subject = request.POST["message-subject"]
        message_email = request.POST["message-email"]
        message = request.POST["message"]

        # send and email
        # send_mail(
        #     message_name + " / " + message_subject + " / " + message_email,  # subject
        #     message,  # message
        #     settings.EMAIL_HOST,  # from email
        #     ["erikutism@gmail.com"],  # To email
        #     fail_silently=False,
        # )

        return render(request, "success.html", {"message_name": message_name})

    else:
        return render(request, "contact.html", {})
