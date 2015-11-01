from django.conf.urls import url

from web_ide.repository.views import StructureView, ContentView

urlpatterns = [
    url(r'^structure/(?P<local_repository_id>[0-9]+)/?$', StructureView.as_view()),
    url(r'^content/?$', ContentView.as_view())
]
