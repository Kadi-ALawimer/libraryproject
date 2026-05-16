from django import forms
# from .models import Book

# class Bookforms(forms.ModelForm):
#     class Meta :
#         model = Book 
#         fields = ['title','author','price','edition']




from .models import (
    S1,
    S2,
    I1
)


class S1Form(forms.ModelForm):

    class Meta:

        model = S1

        fields = [
            'name',
            'age',
            'address'
        ]


class S2Form(forms.ModelForm):

    class Meta:

        model = S2

        fields = [
            'name',
            'age',
            'addresses'
        ]


class I1Form(forms.ModelForm):

    class Meta:

        model = I1

        fields = [
            'name',
            'image'
        ]        


