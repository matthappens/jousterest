from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='pin-index'),
    url(r'^create$', views.create_pin, name='create-pin'),
    url(r'^update$', views.update_pin, name='update-pin'),
    url(r'^delete$', views.delete_pin, name='delete-pin'),
]
