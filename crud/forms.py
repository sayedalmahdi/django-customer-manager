from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Sayed"
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Al Mahdi"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "sayed.almahdi@gmail.com"
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "+8801"
    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "House: 01, Block-A, Road: 1"
    }))

    city = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Sylhet"
    }))

    state = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "BD"
    }))

    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'city',
            'state'
        ]
