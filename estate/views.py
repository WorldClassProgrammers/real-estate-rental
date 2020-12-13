from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 , redirect
from django.urls import reverse
from itertools import chain
from django.core.paginator import Paginator
from django.conf import settings

from .forms import CondoForm, UnitForm

from .models import Unit, Condo, CustomUser, ContactInfo
from .models.condo import CondoImages
from .models.unit import UnitImages
from .models.transit_data import BTS_data, MRT_blue_data, MRT_purple_data
from django.core.mail import send_mail

import googlemaps
from estateSite.settings import EMAIL_HOST_USER


def index(request):
    condo_list = Condo.objects.order_by('name')
    return render(request, 'estate/index.html', {'condo_list': condo_list, 'BTS_data': BTS_data})


def condo(request, condo_id):
    condo = get_object_or_404(Condo, pk=condo_id)
    return render( 
        request, 
        'estate/condo.html', {
            'condo': condo,
            'api_key': settings.GOOGLE_MAPS_API_KEY,
            'BTS_data': BTS_data,
            'MRT_blue_data': MRT_blue_data,
            'MRT_purple_data': MRT_purple_data,
        })


def unit(request, unit_id):
    unit = get_object_or_404(Unit, pk=unit_id)
    condo = Condo.objects.get(name=unit.condo.name)
    return render(request, 'estate/unit.html', {'condo': condo, 'unit': unit})


def condo_listing(request):
    condo_listing = Condo.objects.all()
    paginator = Paginator(condo_listing, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'estate/condo_listing.html', {'condo_listing': condo_listing, 'page_obj': page_obj})


def unit_listing(request):
    unit_listing = Unit.objects.all()
    paginator = Paginator(unit_listing, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'estate/unit_listing.html', {'unit_listing': unit_listing, 'page_obj': page_obj})


def search_nearby_bts(request):
    res = request.POST['dropdownsearch']

    condo_set_list = Condo.objects.order_by('-name')
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    latlon = BTS_data[str(res)]
    lat_lon = latlon.split(',')
    origins = {"lat": float(lat_lon[0]), "lng": float(lat_lon[1])}
    print(origins)
    destinations = []
    cd_id = []
    distance_info = {}
    for condo in condo_set_list:
        destinations.append(condo.address)
        cd_id.append(condo.id)

    matrix = gmaps.distance_matrix(origins, destinations, mode="walking")
    filter_list = []
    for k in range(len(destinations)):
        dist = matrix['rows'][0]['elements'][k]['distance']['value']
        if dist <= 500:  # GT 500 m
            filter_list.append(cd_id[k])
            distance_info.update({Condo.objects.get(id=cd_id[k]).name:dist})

    condo_set_list = Condo.objects.filter(id__in=filter_list)
    return 'near by bts', condo_set_list, 'POST', Unit.objects.none(), res, distance_info


def search_by_amnities(request):
    condo_set_list = Condo.objects.order_by('-name')

    if request.method == 'GET':
        res = request.GET['selectedfield']
        keywords = res.strip('][').split(', ')
        for index, amenity in enumerate(keywords):
            amenity = amenity[1:-1]
            keywords[index] = amenity
            condo_set_list = condo_set_list.filter(amenities__icontains=amenity)
    else:
        keywords = request.POST.getlist('selectedfield')
        for amenity in keywords:
            condo_set_list = condo_set_list.filter(amenities__icontains=amenity)

    return keywords, condo_set_list, 'POST', Unit.objects.none()


def search_by_keywords(request):

    keywords = request.GET['search']
    condo_set_list = Condo.objects.filter(name__icontains=keywords)
    unit_set_list = Unit.objects.filter(title__icontains=keywords)
    return keywords, condo_set_list, unit_set_list, request.method


def search(request):
    unit_set_list = Unit.objects.order_by('-title')
    station = ''
    dist_info = ''
    if request.method == 'GET':
        if 'search' in request.GET:  # by keywords
            keywords, condo_set_list, unit_set_list, method = search_by_keywords(
                request)
        else:  # by checkbox fields
            if 'selectedfield' in request.GET:  # by Amnities
                keywords, condo_set_list, method, unit_set_list = search_by_amnities(
                    request)
            else:  # nearby BTS
                keywords, condo_set_list, method, unit_set_list, station, dist_info = search_nearby_bts(
                    request)
    else:
        if 'selectedfield' in request.POST:  # by Amnities
            keywords, condo_set_list, method, unit_set_list = search_by_amnities(
                request)
        else:
            keywords, condo_set_list, method, unit_set_list, station, dist_info = search_nearby_bts(
                request)

    # if no condo then unit shouldnt be return
    if condo_set_list:
        unit_set_list = unit_set_list.filter(
            still_on_contract=False).exclude(condo__in=condo_set_list)

    posts = list(chain(condo_set_list, unit_set_list))
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'keywords': keywords,
        'station': station,
        'distance_info': dist_info,
        'condo_result': condo_set_list,
        'unit_result': unit_set_list,
        'page_obj': page_obj,
        'posts': posts,
        'method': method,
    }

    return render(request, 'estate/search_results.html', context)


@login_required
def upload_index(request):
    if request.user.role != 2:
        return HttpResponseRedirect(reverse('estate:index'))
    condo_form = CondoForm(prefix='condo')
    unit_form = UnitForm(prefix='unit')
    return render(request, 'estate/upload_index.html', {
        'condo_form': condo_form,
        'unit_form': unit_form,
    })


@login_required
def upload_condo(request):
    condo_form = CondoForm(request.POST, prefix='condo')
    # Bug - Amenities have to checked at least one to valid the form
    if condo_form.is_valid():
        this_condo = condo_form.save()

        if len(request.FILES.getlist('files')) > 0:
            for image in request.FILES.getlist('files'):
                CondoImages.objects.create(condo=this_condo, image=image)
        else:
            CondoImages.objects.create(condo=this_condo, image='https://i.imgur.com/31d1Qdm_d.webp?maxwidth=1520&fidelity=grand')
    else:
        msg = f"Invalid Input!"
        messages.error(request, msg)
        return HttpResponseRedirect(reverse('estate:upload_index'))
    return HttpResponseRedirect(reverse('estate:index'))


@login_required
def upload_unit(request):
    unit_form = UnitForm(request.POST, prefix='unit')
    if unit_form.is_valid():
        this_unit = unit_form.save(commit=False)
        this_unit.owner = request.user
        this_unit.save()

        if len(request.FILES.getlist('files')) > 0:
            for image in request.FILES.getlist('files'):
                UnitImages.objects.create(unit=this_unit, image=image)
        else:
            UnitImages.objects.create(unit=this_unit, image='https://i.imgur.com/31d1Qdm_d.webp?maxwidth=1520&fidelity=grand')
    else:
        msg = f"Invalid Input!"
        messages.error(request, msg)
        return HttpResponseRedirect(reverse('estate:upload_index'))
    return HttpResponseRedirect(reverse('estate:index'))

def contact(request):
    if request.method == "POST":
        unit_id  = request.POST['unit_id']
        unit     = request.POST['unit_title']
        name  = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        unit_owner_id = request.POST['unit_owner_id']

        # owner = CustomUser.objects.filter(first_name=unit_owner)
        owner = get_object_or_404(CustomUser, pk=unit_owner_id)

        # email to inform owner about inquiry made.
        send_mail(
            'There has been an inquiry',
            'There has been an inquiry for a '+ unit + ' unit id ' + unit_id + '. \nFrom '+ email
            + '\n' + message,
            EMAIL_HOST_USER,
            [owner.email], 
            fail_silently=False
        )
        return redirect(reverse('estate:condo', args=[unit_id]))

