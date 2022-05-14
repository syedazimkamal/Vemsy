from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from .models import Help

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'class': 'inputC'
        })
        self.fields["last_name"].widget.attrs.update({
            'class': 'inputC'
        })
        self.fields["username"].widget.attrs.update({
            'class': 'inputC'
        })
        self.fields["email"].widget.attrs.update({
            'class': 'inputC'
        })
        self.fields["password1"].widget.attrs.update({
            'class': 'inputC'
        })
        self.fields["password2"].widget.attrs.update({
            'class': 'inputC'
        })

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2',]

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
