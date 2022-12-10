from django import forms
from . import models

class Form_notes(forms.ModelForm):
    class Meta:
        model = models.Model_notes_of_user
        fields = '__all__'