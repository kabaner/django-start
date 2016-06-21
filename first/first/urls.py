from django.conf.urls import url
from first.view import hello
from first.testdb import testdb
from first import search
from first import search2
from django.contrib import admin

urlpatterns = [
    url('^hello/$', hello),
    url('^testdb/$', testdb),
    url('^search-form/$', search.search_form),
    url('^search/$', search.search),
    url('^search-post/$', search2.search_post),
    url('^admin/', admin.site.urls),
]
