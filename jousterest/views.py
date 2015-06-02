from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("pin-index"))
    else:
        return render(request, "home.html", {})
