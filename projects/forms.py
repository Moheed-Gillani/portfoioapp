from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
class Commentform(ModelForm):
    class Meta:
        model= Comment
        fields=('name','email','Comment','Details')
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
class ReviewForm(ModelForm):
    class Meta:
        model=Reviews
        fields=('name','email','Review')