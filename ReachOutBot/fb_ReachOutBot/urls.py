# ReachOutBot/fb_ReachOutBot/urls.py
from django.conf.urls import include,url
from .views import ReachOutBotView

urlpatterns = [
    url(r'^4f82af3be5a4254fd3300244e7fa20c3f71de58029f11fc606/?$', ReachOutView.as_view())
]
