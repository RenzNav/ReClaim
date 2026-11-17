
from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'quantity', 'estimated_value', 'description']

        labels = {
            'title': 'Listing Title',
            'quantity': 'Number of Containers',
            'estimated_value': 'Estimated Deposit Value (€)',
            'description': 'Additional Details',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Mixed Bottles and Cans'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'estimated_value': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': 0
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Provide additional information about your containers'
            }),
        }
