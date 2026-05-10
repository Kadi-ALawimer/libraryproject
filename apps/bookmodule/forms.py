from django import forms
from .models import BookLab9

class BookLab9Form(forms.ModelForm):
    class Meta:
        model = BookLab9
        fields = ['title', 'price', 'quantity', 'rating']