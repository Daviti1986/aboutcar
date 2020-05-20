from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'cars'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name= 'detail'),
    url(r"Cars/add/$", views.CarCreate.as_view(), name = 'car_add')
]