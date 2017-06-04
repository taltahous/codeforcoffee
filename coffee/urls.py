from django.conf.urls import url
from django.contrib.auth import login
from .views import *

urlpatterns = [

    url(r'^home/$', main, name="home"),
    url(r'^$', login, name="login"),
    url(r'^userlist/$', user_list, name='user_list'),
    url(r'^usercoffees/(?P<user_id>[0-9]+)/$', user_coffees, name='user_coffees'),
    url(r'^sendemail/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', send_email, name='send_email'),
    url(r'^replicateorder/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', replicate_order, name='replicate_order'),

    url(r'^createcoffee/$', createCoffee, name='createCoffee'),
    url(r'^editcoffee/(?P<coffee_id>[0-9]+)/$', editCoffee, name='editCoffee'),
    url(r'^deletecoffee/(?P<coffee_id>[0-9]+)/$', deleteCoffee, name='deleteCoffee'),

    url(r'^deletebean/(?P<bean_id>[0-9]+)/$', deleteBean, name='deleteBean'),
    url(r'^createbean/$', createBean, name='createBean'),
    url(r'^editbean/(?P<bean_id>[0-9]+)/$', editBean, name='editBean'),

    url(r'^deletepowder/(?P<powder_id>[0-9]+)/$', deleteBean, name='deletePowder'),
    url(r'^createpowder/$', createPowder, name='createPowder'),
    url(r'^editpowder/(?P<powder_id>[0-9]+)/$', editBean, name='editPowder'),

    url(r'^deletesyrup/(?P<syrup_id>[0-9]+)/$', deleteSyrup, name='deleteSyrup'),
    url(r'^createsyrup/$', createSyrup, name='createSyrup'),
    url(r'^editsyrup/(?P<syrup_id>[0-9]+)/$', editSyrup, name='editSyrup'),

    url(r'^createorder/(?P<coffee_id>[0-9]+)/$', createOrder, name='createOrder'),

]
