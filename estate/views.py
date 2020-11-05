
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Room, Condo


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
    condo = Condo.objects.filter(name=room.condo)[0]
    return render(request, 'estate/room.html', {'condo': condo, 'room': room})


def search(request):
    condoSet_list = Condo.objects.order_by('-name')
    roomSet_list = Room.objects.order_by('-title')

    keywords = request.GET['search']
    condoSet_list = Condo.objects.filter(name__icontains=keywords)
    roomSet_list = Room.objects.filter(title__icontains=keywords)
    context = {
        'condo_result': condoSet_list,
        'room_result': roomSet_list,
    }

    return render(request, 'estate/search_results.html', context)
