from django import forms
from django.contrib.auth.models import User
from NLP.models import NLP_MAPS, Organisation

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ('organisation',)