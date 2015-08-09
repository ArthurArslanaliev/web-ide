from django.conf.urls import url

from web_ide.github.views import AuthView, CallbackView, LogoutView, RepositoriesView

urlpatterns = [
    url(r'^auth/?$', AuthView.as_view()),
    url(r'^callback/?$', CallbackView.as_view()),
    url(r'^logout/?$', LogoutView.as_view()),

    url(r'^repos/?$', RepositoriesView.as_view()),
]
