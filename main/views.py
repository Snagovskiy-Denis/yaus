from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.edit import FormView
from django.contrib import messages

from main.forms import URLShortenerForm
from main.models import URL


class RedirectByShortURL(View):
    http_method_names = ['get']

    def get(self, request, short_url):
        url = get_object_or_404(URL, short=short_url)
        return redirect(url.full)


class HomePage(FormView):
    template_name = 'main/home.html'
    form_class = URLShortenerForm

    def form_valid(self, form):
        url = form.save()
        msg = f'{url.full} -> is shortened to -> {url.get_short()}'
        messages.success(self.request, msg)
        return redirect('/')
