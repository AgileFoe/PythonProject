from .models import discribe
from django.forms import ModelForm, TextInput, FileInput, Textarea

class DiscribeForm(ModelForm):
    class Meta:
        model = discribe
        fields = ['title', 'anons', 'full_text', 'image']

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "news",
            }),
            "anons": TextInput(attrs={
                "class": "form-control",
                "placeholder": "anons",
            }),
            "image": FileInput(attrs={
                "class": "form-control",
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "full text",
            })
        }

