from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

#class for the login
class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input", 'placeholder': '**************', 'id': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input", 'placeholder': '**************', 'id': 'password'}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password"]:
            self.fields[fieldname].help_text = None
        
    class Meta:
        model = User
        fields = ("username" , "password")

#class for the register
class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input", 'placeholder': '*************', 'id': 'username'})
    )
    password1 = forms.CharField(widget=forms.PasswordInput( 
        attrs={'class': "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input", 'placeholder': '********', 'id': 'password'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input", 'placeholder': '********', 'id': ' password'})
    )

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None
                    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")