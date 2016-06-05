from django.conf.urls import url

from . import views

app_name = 'blogit'

urlpatterns = [
    url(r'^(?P<slug>[-\w]*)/$', views.view_blog_post, name='view_blog_post')
]
