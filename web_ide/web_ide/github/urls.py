from django.conf.urls import url

from web_ide.github.views import AuthView, CallbackView, LogoutView, RepositoriesView, RepositoryView

urlpatterns = [
    url(r'^auth/?$', AuthView.as_view()),
    url(r'^callback/?$', CallbackView.as_view()),
    url(r'^logout/?$', LogoutView.as_view()),

    url(r'^repos/?$', RepositoriesView.as_view()),
    url(r'^repos/(?P<repository_id>[0-9]+)/?$', RepositoryView.as_view())
]
