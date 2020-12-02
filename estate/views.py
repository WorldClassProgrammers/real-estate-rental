from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from itertools import chain
from django.core.paginator import Paginator
from django.conf import settings

from .forms import CondoForm, UnitForm
from .models import Unit, Condo
from .models.condo import CondoImages
from .models.unit import UnitImages
from .models.transit_data import BTS_data, MRT_blue_data, MRT_purple_data  


class IndexView(generic.ListView):
    template_name = 'estate/index.html'
    condo_list = 'condo_list'

    def get_queryset(self):
        return Condo.objects.order_by('name')


def condo(request, condo_id):
    condo = get_object_or_404(Condo, pk=condo_id)
    return render(request, 'estate/condo.html', {'condo': condo,
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


def search_by_amnities(request):
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

    return keywords, condoSet_list, 'POST', Unit.objects.none()


def search_by_keywords(request):

    keywords = request.GET['search']
    condoSet_list = Condo.objects.filter(name__icontains=keywords)
    unitSet_list = Unit.objects.filter(title__icontains=keywords)
    return keywords, condoSet_list, unitSet_list, request.method


def search(request):
    unitSet_list = Unit.objects.order_by('-title')

    if request.method == 'GET':
        if 'search' in request.GET:  # by keywords
            keywords, condoSet_list, unitSet_list, method = search_by_keywords(
                request)
        else:  # by checkbox fields
            keywords, condoSet_list, method, unitSet_list = search_by_amnities(
                request)
    else:
        keywords, condoSet_list, method, unitSet_list = search_by_amnities(
            request)

    # if no condo then unit shouldnt be return
    if condoSet_list:
        unitSet_list = unitSet_list.filter(
            still_on_contract=False).exclude(condo__in=condoSet_list)


    posts = list(chain(condoSet_list, unitSet_list))
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'keywords': keywords,
        'condo_result': condoSet_list,
        'unit_result': unitSet_list,
        'page_obj': page_obj,
        'posts': posts,
        'method': method,
    }

    return render(request, 'estate/search_results.html', context)


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

        for image in request.FILES.getlist('files'):
            CondoImages.objects.create(condo=this_condo, image=image)

    return HttpResponseRedirect(reverse('estate:index'))


@login_required
def upload_unit(request):
    unit_form = UnitForm(request.POST, prefix='unit')
    if unit_form.is_valid():
        this_unit = unit_form.save(commit=False)
        this_unit.owner = Owner.objects.first()
        this_unit.save()

        for image in request.FILES.getlist('files'):
            UnitImages.objects.create(unit=this_unit, image=image)
    else:
        print("==========unit_form_invalid===========", request.POST)

    return HttpResponseRedirect(reverse('estate:index'))
