from django import forms
from .models import Book  # Import your model if you need to use model fields

class ExampleForm(forms.Form):
    # Define form fields here
    title = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=100, required=True)
    publication_year = forms.IntegerField(required=True)
    # Add any other fields you need