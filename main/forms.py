from django.forms import ModelForm, widgets

from main.models import URL


class URLShortenerForm(ModelForm):
    class Meta:
        model = URL
        fields = ('full', 'short')
        widgets = {
            'full':
            widgets.URLInput(
                attrs={'placeholder': 'Enter a URL to shorten...'}),
            'short':
            widgets.TextInput(attrs={'placeholder': 'Optional beautiful name'})
        }
