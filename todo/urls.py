from django.conf.urls import url
from django.contrib import admin
from .views import home, detail, add_todo, update_todo, \
	 delete_todo, mark_complete

urlpatterns = [
    url(r'^$', home, name='todos'),
    url(r'^add/$', add_todo, name='create'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^(?P<pk>\d+)/update/$', update_todo, name='update'),
    url(r'^(?P<todo_id>\d+)/delete/$', delete_todo, name='delete'),
    url(r'^(?P<todo_id>\d+)/mark-complete/$', mark_complete, name='mark_complete')
]
