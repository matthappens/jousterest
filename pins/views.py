from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Pin
from .forms import PinForm


@login_required
def index(request):
    """ return a paginated list of Pins
    """
    pin_objects = Pin.objects.filter(user=request.user)
    paginator = Paginator(pin_objects, request.GET.get('count', settings.DEFAULT_PAGINATION))
    page = request.GET.get('page', 1)

    try:
        pins = paginator.page(page)
    except EmptyPage:
        pins = paginator.page(paginator.num_pages)
    context = {
        "pins": pins,
        "pin_form": PinForm,
        "page": page,
        "num_pages": paginator.num_pages
    }
    return render(request, "pins/index.html", context)


@login_required
@require_POST
def create_pin(request):
    pin = Pin(user=request.user)
    form = PinForm(request.POST, instance=pin)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("pin-index"))


@login_required
@require_POST
def update_pin(request, pin_id):
    pin = get_object_or_404(Pin, pk=pin_id)
    form = PinForm(request.POST, pin)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse("pin-index"))


@login_required
@require_POST
@csrf_exempt
def delete_pin(request, pin_id):
    pin = get_object_or_404(Pin, pk=pin_id)
    pin.delete()
    return HttpResponseRedirect(reverse("pin-index"))
