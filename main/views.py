from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from main.models import URL


class RedirectByShortURL(View):
    http_method_names = ['get']

    def get(self, request, short_url):
        url = get_object_or_404(URL, short=short_url)
        return redirect(url.full)
