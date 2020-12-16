from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, Unit, CondoImages, UnitImages, CustomUser, ContactInfo


class TestSearch(TestCase):

    def test_search_found(self):
        condo = Condo.objects.create(name="The villa", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345', address="Bangkok, ประเทศไทย")
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        url = "{url}?{filter}={value}".format(url=reverse("estate:search_results"), filter='search', value='The')
        response = self.client.get(url)
        print(url)
        self.assertContains(response, 'The villa')

    def test_search_not_found(self):
        condo = Condo.objects.create(name="The villa", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345', address="Bangkok, ประเทศไทย")
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        url = "{url}?{filter}={value}".format(url=reverse("estate:search_results"), filter='search', value='Theee')
        response = self.client.get(url)
        print(url)
        self.assertNotContains(response, 'The villa')

    def test_search_by_none_amenity(self):
        condo = Condo.objects.create(name="The villa", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345', address="Bangkok, ประเทศไทย")
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        url = reverse("estate:search_results")
        response = self.client.get(url)
        self.assertNotContains(response, 'The villa')

