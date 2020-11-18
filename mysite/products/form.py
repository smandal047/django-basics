from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """override field"""
    title = forms.CharField(label='titlE', widget=forms.TextInput(attrs={
        "placeholder": "Your Title"}))

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'summary', 'featured']

    """ field validation"""
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'dm' not in title:
            raise forms.ValidationError("This is not a valid title")

        return title

"""
    https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
    Creating forms from models
"""
