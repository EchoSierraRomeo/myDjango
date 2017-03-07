from django.conf.urls import url
from LFApp import views

app_name = 'LFApp'

urlpatterns = [
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relative,name='relative'),
]
