from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            return HttpResponseRedirect(reverse("pin-index"))
    return HttpResponseRedirect(reverse("jousterest-home"))


def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse("jousterest-home"))
