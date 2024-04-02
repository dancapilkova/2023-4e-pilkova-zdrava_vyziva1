from django import forms
from .models import Profile
from django.forms.widgets import DateInput

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "bio", 'dob']
        labels = {"image": "Profile Picture", "bio": "Bio", 'dob': "Date of Birth"}
        widgets = {
        'dob': DateInput(attrs={'type': 'date'})
    }