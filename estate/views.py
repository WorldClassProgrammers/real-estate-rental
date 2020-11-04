from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .forms import OwnerForm
from .models import Room, Condo, Owner


class IndexView(generic.ListView):
    template_name = 'estate/index.html'
    # room_list = 'room_list'
    condo_list = 'condo_list'

    def get_queryset(self):
        return Condo.objects.order_by('name')


def condo(request, condo_id):
    condo = get_object_or_404(Condo, pk=condo_id)
    return render(request, 'estate/condo.html', {'condo': condo})


def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    condo = Condo.objects.get(name=room.condo.name)
    return render(request, 'estate/room.html', {'condo': condo, 'room': room})


@login_required
def upload_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('estate:index'))
    else:
        form = OwnerForm()
    return render(request, 'estate/upload_owner.html', {'form': form})
