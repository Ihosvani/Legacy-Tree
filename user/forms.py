from user.password_validator import NumberValidator, UppercaseValidator, LowercaseValidator, SymbolValidator, MinimumLengthValidator
from django.core.exceptions import ValidationError
from django import forms
from .models import User

class User_Form(forms.ModelForm):
    
    class Meta:
        model = User
        required_css_class = 'is-strong'
        error_css_class = 'has-text-danger'
        fields = ("username", "first_name", "last_name", "email", "password", "date_of_birth")
        widgets={
            'date_of_birth': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'username': forms.widgets.TextInput(attrs={'class':'input'}),
            'first_name': forms.widgets.TextInput(attrs={'class':'input'}),
            'last_name': forms.widgets.TextInput(attrs={'class':'input'}),
            'email': forms.widgets.TextInput(attrs={'class':'input'}),
            'password': forms.widgets.TextInput(attrs={'class':'input'}),
        }
    
    def clean(self):
 
        # data from the form is fetched using super function
        super(User_Form, self).clean()
         
        # extract the username and text field from the data
        password = self.cleaned_data.get('password')
        length_validator = MinimumLengthValidator()

        try:

            length_validator.validate(password=password)
            NumberValidator.validate(password=password)
            UppercaseValidator.validate(password=password)
            LowercaseValidator.validate(password=password)
            SymbolValidator.validate(password=password)

        except ValidationError as e:
            
            self.errors['password'] = self.error_class([
                e])
    
        