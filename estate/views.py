from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .forms import OwnerForm, CondoForm, RoomForm
from .forms.condo_form import CondoImagesForm
from .forms.room_form import RoomImagesForm
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

@login_required
def upload_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('estate:index'))
    else:
        form = OwnerForm()
    return render(request, 'estate/upload_owner.html', {'form': form})


@login_required
def upload_index(request):
    condo_form = CondoForm()
    room_form = RoomForm()
    condo_images_form = CondoImagesForm()
    room_images_form = RoomImagesForm()
    return render(request, 'estate/upload_index.html', {
        'condo_form': condo_form,
        'room_form': room_form,
        'condo_images_form': condo_images_form,
        'room_images_form': room_images_form,
    })


def upload_condo(request):

    condo_form = CondoForm(request.POST)
    c = condo_form.save()

    # # for i in range(request.POST.get('number_of_images')):
    # condo_images_form = CondoImagesForm(request.POST)
    # condo_images_form.save(commit=False)
    # condo_images_form.condo = c
    # condo_images_form.save()
    return HttpResponseRedirect(reverse('estate:index'))


def upload_room(request):
    room_form = RoomForm(request.POST)
    # room_form.save(commit=False)
    # room_form.owner = request.user.owner_set.first()
    room_form.save()
    return HttpResponseRedirect(reverse('estate:index'))
