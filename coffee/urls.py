from django.conf.urls import url
from django.contrib.auth import login
from .views import *

urlpatterns = [

   url(r'^$', main, name="home"),
    url(r'^createcoffee/$', createCoffee, name='createCoffee'),
    url(r'^editcoffee/(?P<coffee_id>[0-9]+)/$', editCoffee, name='editCoffee'),
    url(r'^editbean/(?P<bean_id>[0-9]+)/$', editBean, name='editBean'),
    url(r'^createbean/$', createBean, name='createBean'),
    url(r'^deletecoffee/(?P<coffee_id>[0-9]+)/$', deleteCoffee, name='deleteCoffee'),
    url(r'^deletebean/(?P<bean_id>[0-9]+)/$', deleteBean, name='deleteBean'),

]