from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from estate.models import Room, Condo


class IndexView(generic.ListView):
    template_name = 'estate/index.html'
    room_list = 'room_list'

    def get_queryset(self):
        return Room.objects.filter(
            still_on_contract=False
        )


def condo(request, condo_id):
    condo = get_object_or_404(Condo, pk=condo_id)
    return render(request, 'estate/condo.html', {'condo': condo})


def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    condo = Condo.objects.filter(condo_name=room.condo_name)[0]
    return render(request, 'estate/room.html', {'condo': condo, 'room': room})
