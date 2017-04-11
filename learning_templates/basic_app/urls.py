from django.conf.urls import url
from basic_app import views

# Template Tagging
app_name = 'basic_app' #must be app_name

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]
