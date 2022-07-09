from django import forms
from django.forms import inlineformset_factory

from .models import Customer


class CustomerForm(forms.ModelForm):
    """model form of Customer"""

    class Meta:
        model = Customer
        fields = (
            'name',
            'email',
            'phone',
            'address',
        )
