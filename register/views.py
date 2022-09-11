from django.shortcuts import render
from user.forms import User_Form
from user.password_validator import NumberValidator, UppercaseValidator, LowercaseValidator, SymbolValidator, MinimumLengthValidator
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
# Create your views here.

def register_view(request):
    user_form = User_Form(request.POST or None)
    next_page = 'registration.html'
    context = {}
    context['user_form'] = user_form

    if not user_form.is_valid():
        print('form is not valid')
        context['user_form_errors'] = user_form.errors
        
    else:
        print('form is valid')
        user_form.save()
        return redirect('/login/')
        
    return render(request, next_page, context=context)