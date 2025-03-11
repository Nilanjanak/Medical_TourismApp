from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
 username = forms.CharField()
 password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text="Enter a strong password."
    )
    password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput,
        help_text="Enter the same password for confirmation."
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'email': 'Email Address',
        }
        help_texts = {
            'username': 'Enter a unique username.',
            'email': 'Provide a valid email address.',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
