from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html"), name="jousterest-home"),
    url(r'^pins/', include('pins.urls')),
    url(r'^auth/', include('jousterest.site.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
