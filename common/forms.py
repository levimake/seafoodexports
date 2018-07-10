from crispy_forms.bootstrap import InlineField

from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        widgets = {
                    'address': forms.Textarea(attrs = {'rows': 3})
                  }
        
        exclude = ['id', 'username', 'email', 'completed']


class AddressForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
                    'address': forms.Textarea(attrs = {'rows': 3})
                  }

        fields = ['address']


class PasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


class PhoneForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number']
