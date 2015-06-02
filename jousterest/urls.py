from django.conf.urls import include, url
from django.contrib import admin
from .views import index

urlpatterns = [
    url(r'^$', index, name="jousterest-home"),
    url(r'^pins/', include('pins.urls')),
    url(r'^auth/', include('jousterest.site.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
