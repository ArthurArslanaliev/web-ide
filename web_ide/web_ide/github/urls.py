from django.conf.urls import url

from web_ide.github.views import AuthView, CallbackView, LogoutView, RepositoriesView, RepositoryView

urlpatterns = [
    url(r'^auth/?$', AuthView.as_view()),
    url(r'^callback/?$', CallbackView.as_view()),
    url(r'^logout/?$', LogoutView.as_view()),

    url(r'^repos/?$', RepositoriesView.as_view()),
    # the repository_name can consists of any characters
    url(r'^repos/(?P<repository_name>.+)/?$', RepositoryView.as_view())
]
