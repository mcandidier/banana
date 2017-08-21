from django.conf.urls import url
from django.contrib import admin
from .views import home, detail, update_todo, \
	 delete_todo, mark_complete, TodoView, LatestPost, TodoFormView, json_todos

urlpatterns = [
    url(r'^$', home, name='todos'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^(?P<pk>\d+)/update/$', update_todo, name='update'),
    url(r'^(?P<todo_id>\d+)/delete/$', delete_todo, name='delete'),
    url(r'^(?P<todo_id>\d+)/mark-complete/$', mark_complete, name='mark_complete'),
    url(r'^ajax/list/$', json_todos, name='json_todos'),


    # class based views
    url(r'^add/$', TodoFormView.as_view(), name='todo_form'),
    url(r'^ajax/$', TodoView.as_view(), name='ajax_todos'),
    url(r'^ajax/latest/posts/$', LatestPost.as_view(), name='ajax_latest_posts'),
]
