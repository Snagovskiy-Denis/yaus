from django.urls.conf import path
from django.views.decorators.csrf import csrf_exempt

from . import views, api

urlpatterns = [
        path('', views.HomePage.as_view()),
        path('api/', csrf_exempt(api.CreateShortURL.as_view())),
        path('<slug:short_url>', views.RedirectByShortURL.as_view()),
]
