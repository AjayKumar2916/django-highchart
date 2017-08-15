from django.conf.urls import url

from chart import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]