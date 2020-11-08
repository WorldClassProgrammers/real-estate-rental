
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from itertools import chain
from django.core.paginator import Paginator

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

def search_by_amnities(request ):
    condoSet_list = Condo.objects.order_by('-name')

    if request.method == 'GET':        
        res = request.GET['selectedfield']
        keywords = res.strip('][').split(', ')
        for index, amenity in enumerate(keywords):
            # remove quotes at begin and end. Somehow strip doesnt work
            # and update back to keywords.

            amenity = amenity[1:-1]
            keywords[index] = amenity
            condoSet_list = condoSet_list.filter(amenities__icontains=amenity)
    else:
        keywords = request.POST.getlist('selectedfield')
        for amenity in keywords:
            condoSet_list = condoSet_list.filter(amenities__icontains=amenity)

    return keywords, condoSet_list, 'POST', Room.objects.none()

def search_by_keywords( request ):

    keywords = request.GET['search']
    condoSet_list = Condo.objects.filter(name__icontains=keywords)
    roomSet_list = Room.objects.filter(title__icontains=keywords)
    return keywords , condoSet_list , roomSet_list , request.method

def search(request):
    roomSet_list = Room.objects.order_by('-title')

    if request.method == 'GET':
        if 'search' in request.GET: # by keywords
            keywords , condoSet_list , roomSet_list, method = search_by_keywords(request)
        else: # by checkbox fields
            keywords, condoSet_list,method, roomSet_list = search_by_amnities(request )
    else:
        keywords, condoSet_list, method, roomSet_list = search_by_amnities( request)

    # if no condo then room shouldnt be return
    if condoSet_list:
        roomSet_list = roomSet_list.filter(
            still_on_contract=False).exclude(condo__in=condoSet_list)
    else:
        roomSet_list = Room.objects.none()

    posts = list(chain(condoSet_list, roomSet_list))
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'keywords': keywords,
        'condo_result': condoSet_list,
        'room_result': roomSet_list,
        'page_obj': page_obj,
        'posts': posts,
        'method' : method,
    }

    return render(request, 'estate/search_results.html', context)
