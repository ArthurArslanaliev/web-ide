from django.conf.urls import url

from web_ide.repository.views import StructureView, ContentView, CreateEntityView, RenameEntityView

# TODO: Change the order of repository_id & structure keyword
urlpatterns = [
    url(r'^structure/(?P<local_repository_id>[0-9]+)/?$', StructureView.as_view()),
    url(r'^structure/(?P<local_repository_id>[0-9]+)/create/?$', CreateEntityView.as_view()),
    url(r'^structure/(?P<local_repository_id>[0-9]+)/rename/?$', RenameEntityView.as_view()),
    url(r'^content/?$', ContentView.as_view())
]
