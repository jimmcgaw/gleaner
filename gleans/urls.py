from django.conf.urls import url

from . import views

app_name = 'gleans'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^account/$', views.user_home, name='user_home'),
    url(r'^account/gleans/$', views.gleanlist, name='gleanlist'),
]
