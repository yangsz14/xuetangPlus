from django import forms
from .models import*
from django.contrib.auth.models import User

class ReplyForm(forms.ModelForm):
    class Meta:
        model = BBSPost
        fields = ('P_Title','P_Content')