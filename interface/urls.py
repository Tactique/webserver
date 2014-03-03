from django.conf.urls import patterns, url

from interface import views

urlpatterns = patterns('',
    url(r'^tests/$', views.tests, name='tests'),
    url(r'^editor/$', views.editor, name='editor'),
    url(r'play/$', views.index, name='index'),
)
