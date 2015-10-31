from django.conf.urls import include, url
from django.contrib import admin

from web_ide.views import Index

urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^api/github/', include('web_ide.github.urls')),
    url(r'^api/repository/', include('web_ide.repository.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
