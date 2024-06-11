from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django import forms

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class UserPassChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class UserPassChangeForm2(SetPasswordForm):
    class Meta:
        model = User
        fields = '__all__'