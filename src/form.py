from django import forms
from sethu.models import login

class loginModel(forms.ModelForm):
    class Meta:
        model=login
        fields="__all__"

