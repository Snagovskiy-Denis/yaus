from django.forms import ModelForm, widgets

from main.models import URL


class URLShortenerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = URL
        fields = ('full', 'short')
        widgets = {
            'full':
            widgets.URLInput(
                attrs={
                    'placeholder': 'Enter a URL to shorten...',
                    'class': 'form-control'
                }),
            'short':
            widgets.TextInput(attrs={
                'placeholder': 'Optional beautiful name',
                'class': 'form-control'
            })
        }
        labels = {
            'full': 'Enter a URL to shorten',
            'short': 'Optional beutiful name'
        }
