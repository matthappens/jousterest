from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Pin
from .forms import PinForm


@login_required
def index(request):
    """ return a paginated list of Pins
    """
    pin_objects = Pin.objects.all()
    paginator = Paginator(pin_objects, request.GET.get('count', settings.DEFAULT_PAGINATION))
    page = request.GET.get('page')

    try:
        pins = paginator.page(page)
    except PageNotAnInteger:
        pins = paginator.page(1)
    except EmptyPage:
        pins = paginator.page(paginator.num_pages)
    context = {
        "pins": pins,
        "pin_form": PinForm
    }
    return render(request, "pins/index.html", context)


@login_required
@require_POST
def create_pin(request):
    form = PinForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("pin-index"))


@login_required
@require_POST
def update_pin(request, pin_id):
    try:
        pin = Pin.objects.get(pk=pin_id)
        form = PinForm(request.POST, pin)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("pin-index"))
    except Pin.DoesNotExist:
        pass  # @TODO return appropriate error


@login_required
@require_POST
def delete_pin(request, pin_id):
    try:
        pin = Pin.objects.get(pk=pin_id)
        pin.delete()
    except Pin.DoesNotExist():
        pass  # @TODO return appropriate error
