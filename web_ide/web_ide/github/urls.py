from django.conf.urls import include, url
from web_ide.github.views import LoginView

urlpatterns = [
    url(r'^login/?$', LoginView.as_view()),
]
