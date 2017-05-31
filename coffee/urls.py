from django.conf.urls import url
from django.contrib.auth import login
from views import createCoffee
from
from .views import *

urlpatterns = [

   url(r'^$', main, name="home"),
    url(r'^createcoffee', createCoffee, name='createCoffee'),
    url(r'^editcoffee/(?P<coffee_id>[0-9]+)/$', editCoffee, name='editCoffee'),

]