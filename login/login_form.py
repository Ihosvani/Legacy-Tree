from django import forms
from user.password_validator import NumberValidator, UppercaseValidator, LowercaseValidator, SymbolValidator, MinimumLengthValidator

# Create your forms here.

class Login_form(forms.Form):
	email_or_username = forms.CharField(max_length=100, widget=forms.TextInput(
		attrs={
			"class" : "input"
		}))
	password = forms.CharField(max_length=100, validators=[NumberValidator, UppercaseValidator, LowercaseValidator, SymbolValidator, MinimumLengthValidator], widget=forms.TextInput(
		attrs={
			"class" : "input"
		}
	))