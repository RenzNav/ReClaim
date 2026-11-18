# Imports for ListingForm
from django import forms
from .models import Listing

# Imports for RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


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


class RegisterForm(UserCreationForm):
    # Require an email address during registration
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

    # Apply Bootstrap styling to the registration fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    
    # Prevent users from registering with an existing email
    def clean_email(self):
        email = self.cleaned_data['email']

        if get_user_model().objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email
