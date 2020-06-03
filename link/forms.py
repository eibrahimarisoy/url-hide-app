from django.forms import ModelForm

from .models import Link


class LinkCreationForm(ModelForm):

    class Meta:
        model = Link
        fields = ['exact_link']

    def __init__(self, *args, **kwargs):
        super(LinkCreationForm, self).__init__(*args, **kwargs)

        self.fields['exact_link'].widget.attrs['placeholder'] = "http://..."


class LinkForwardForm(ModelForm):

    class Meta:
        model = Link
        fields = ['hide_link']
    
    def __init__(self, *args, **kwargs):
        super(LinkForwardForm, self).__init__(*args, **kwargs)
        self.fields['hide_link'].widget.attrs['readonly'] = True
