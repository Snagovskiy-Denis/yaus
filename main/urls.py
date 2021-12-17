from django.urls.conf import path

from . import views

urlpatterns = [
        path('', lambda request: None),
        path('<slug:short_url>/', lambda request: None),

        path('api/', lambda request: None),
        path('api/<slug:short_url>/', lambda request: None),
]
