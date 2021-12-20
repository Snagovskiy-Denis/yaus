from django.urls.conf import path

from . import views, api

urlpatterns = [
        path('', lambda request: None),
        path('api/', api.CreateShortURL.as_view()),
        path('<slug:short_url>', views.RedirectByShortURL.as_view()),
]
