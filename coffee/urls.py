from django.conf.urls import url
from django.contrib.auth import login

from .views import *

urlpatterns = [
    url(r'^main/', main, name="name"),
    url(r'^$', login, name="login"),

]
