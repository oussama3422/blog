from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
        # Add Crispy Forms helper
        helper = FormHelper()
        helper.form_method = 'post'
        helper.add_input(Submit('submit', 'Update', css_class='btn btn-outline-primary'))

        


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']
