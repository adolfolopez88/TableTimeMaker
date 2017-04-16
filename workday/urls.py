from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.hello_world, name='hello'),
    url(r'^workday/(?P<pk>[0-9]+)/$', views.workday_detail, name='workday_detail'),
    url(r'^workday/new', views.new_workday, name='new_workday')
]