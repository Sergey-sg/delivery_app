from django import forms
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from .models import Customer


class CustomerForm(forms.ModelForm):
    """model form of Customer"""

    class Meta:
        model = Customer
        fields = (
            'address',
            'geolocation',
            'name',
            'email',
            'phone',
        )
        widgets = {
            'address': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap', 'style': 'width: 60%'}),
            'geolocation': forms.HiddenInput()
        }
