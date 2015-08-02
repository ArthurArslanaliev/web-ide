from django.conf.urls import url

from web_ide.github.views import AuthView, CallbackView, LogoutView

urlpatterns = [
    url(r'^auth/?$', AuthView.as_view()),
    url(r'^callback/?$', CallbackView.as_view()),
    url(r'^logout/?$', LogoutView.as_view())
]
