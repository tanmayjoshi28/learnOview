from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User, auth


def startPage(request):
    return render(request, 'users/index2.html')


def Login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("videoCategories:homepage"))
        else:
            context["error"] = "Provide Valid Credentials"
            return render(request, "users/index2.html", context)
    else:
        return render(request, "users/index2.html", context)


def Register(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 and password1 != '':
            if User.objects.filter(username=user_name).exists():
                context['error2'] = 'Username Taken'
                return render(request, "users/index2.html", context)
            elif User.objects.filter(email=email).exists():
                context['error2'] = 'E-Mail Already in use'
                return render(request, "users/index2.html", context)
            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email, first_name = first_name, last_name = last_name)
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse("videoCategories:homepage"))
        else:
            context['error2'] = 'Passwords did not Match'
            return render(request, "users/index2.html", context)
    else:
        return render(request, "users/index2.html")


def Logout(request):

    pass