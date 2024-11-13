# forms.py

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        labels = {
            'comment': 'Your Review',
            'rating': 'Your Rating (0 to 5)'
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 0.5})
        }
