from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Your Username', 'class': 'w-full py-4 px-6 rounded-xl'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']