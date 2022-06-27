"""Defines URL schemes for learning_logs."""
from xml.etree.ElementInclude import include
from django.urls import re_path as url

from . import views


urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),

    # output all topics
    url(r'^topics/$', views.topics, name='topics'),

    # Page with detailed information on a particular topic
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]