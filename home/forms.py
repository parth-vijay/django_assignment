from django import forms
from .models import *

class AreaKeyForm(forms.ModelForm):
    class Meta:
        model = AreaKey
        fields = ('file',)