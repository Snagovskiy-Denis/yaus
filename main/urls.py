from django.urls.conf import path

from . import views, api

urlpatterns = [
        path('', lambda request: None),

        path('api/', api.CreateShortURL.as_view()),
        path('api/<slug:short_url>', lambda request, short_url: None),

        path('<slug:short_url>', lambda request, short_url: None),
]
