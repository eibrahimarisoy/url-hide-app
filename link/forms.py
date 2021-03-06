from django.forms import ModelForm

from .models import Link


class LinkCreationForm(ModelForm):

    class Meta:
        model = Link
        fields = ['exact_link']

    def __init__(self, *args, **kwargs):
        super(LinkCreationForm, self).__init__(*args, **kwargs)
        self.fields['exact_link'].widget.attrs['placeholder'] = "http://..."



