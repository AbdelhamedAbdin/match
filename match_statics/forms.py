from django import forms
from .models import Statistics


class StaticForm(forms.ModelForm):

    class Meta:
        model = Statistics
        fields = '__all__'
        exclude = ['main']
