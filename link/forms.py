from django import forms
from django.forms import ModelForm

from .models import Link
from django.forms.fields import URLField

class LinkCreationForm(ModelForm):

    class Meta:
        model = Link
        fields = ['exact_link', 'hide_link']

    def __init__(self, *args, **kwargs):
        super(LinkCreationForm, self).__init__(*args, **kwargs)

        self.fields['exact_link'].widget.attrs['placeholder'] = "http://..."
        self.fields['hide_link'].required = False
        self.fields['hide_link'].widget.attrs['readonly'] = True