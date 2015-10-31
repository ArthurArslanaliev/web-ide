from django.conf.urls import url

from web_ide.github.views import AuthView, CallbackView, LogoutView, RepositoriesView, RepositoryView

urlpatterns = [
    url(r'^structure/?$', AuthView.as_view())
]
