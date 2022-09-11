from django.shortcuts import render
from login.login_form import Login_form
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
    
def login_view(request, *args, **kwargs):
    context={}
    if request.method == 'POST':
        #user not found by email
        user = authenticate(request=request, email=request.POST['email_or_username'], username=request.POST['email_or_username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.success(request, ('There was an error loggin in, try again with different credentials'))
            return redirect('/login/')

    login_form = Login_form(request.POST or None)
    context['login_form'] = login_form
    if login_form.is_valid():
        login_form.save()
    return render(request, 'login.html', context=context)
