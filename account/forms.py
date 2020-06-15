from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    preferences = forms.CharField(max_length=30, required=False, help_text='Put your Preference comma seperated.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',"preferences", )

class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'preferences', 'username', 'birth_date', 'avatar')
