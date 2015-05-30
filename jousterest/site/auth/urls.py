from django.conf.urls import url
from .views import login
from .views import logout

urlpatterns = [
    url(r'^login$', login, name='user-login'),
    url(r'^logout$', logout, name='user-logout'),
]
