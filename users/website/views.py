from django.shortcuts import render, redirect
from .models import User
from django.core.urlresolvers import reverse
from .decorators import login_required


def login(request):
    session_username = request.session.get('username', False)
    if session_username:
        return redirect(reverse('profile'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        u = User.login(username, password)

        if u is None:
            error = 'Wrong username/password'
        else:
            request.session['username'] = username
            return redirect(reverse('profile'))

    return render(request, 'login.html', locals())


def register(request):
    session_username = request.session.get('username', False)
    if session_username:
        return render(request, 'profile.html')
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeatpassword']:
            username = request.POST['username']
            password = request.POST['password']
            user = User(username, password)
            user.save()
    return render(request, 'register.html')


def home(request):
    return render(request, 'login.html')


@login_required(redirect_url='login')
def profile(request):
    # session_username = request.session.get('username', False)
    if request.method == 'POST':
        del request.session['username']
        request.session.modified = True
        return redirect('home')
    # if session_username:
        # return render(request, 'profile.html')
    # return redirect(reverse('login'))
# Create your views here.
    