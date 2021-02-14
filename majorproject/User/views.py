from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "user/index.html")


@login_required
def special(request):
    return  HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse("index"))
    return redirect('MPHome')



def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in.')
            return redirect('Login')
        else:
            form = UserForm()
            messages.error(request,f'Invalid Username or password')
    return render(request, 'user/registration.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                # return HttpResponseRedirect(reverse('index'))
                return redirect('MPHome')

            else:
                return HttpResponse("Your account was inactive.")
        else:
            messages.error(request, f'Someone tried to login and failed.')
            messages.error(request, "They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user/login.html', {})


