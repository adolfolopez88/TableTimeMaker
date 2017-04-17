from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^workday$', views.WorkdayList.as_view(), name='workday_list'),
    url(r'^workday/(?P<pk>[0-9]+)/$', views.WorkdayDetail.as_view(), name='detail'),
    url(r'^workday/new', views.new_workday, name='new_workday')
]