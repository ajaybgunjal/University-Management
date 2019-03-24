from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import Group

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # first_name = forms.CharField(max_length=100, required=True, str = "First Name")
    # last_name = forms.CharField(max_length=100, required=True, str = "Last Name")
    # group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'groups', 'password1', 'password2']