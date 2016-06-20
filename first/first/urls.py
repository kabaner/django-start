from django.conf.urls import url
from first.view import hello
from first.testdb import testdb

urlpatterns = [
    url('^hello/$', hello),
    url('^testdb/$', testdb),
]
