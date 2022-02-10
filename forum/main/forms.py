from .models import Info
from django.forms import ModelForm, TextInput, Textarea


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ("title", "info")
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввидите название'
            }),
            "info": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ввидите информацию'
            }),
        }