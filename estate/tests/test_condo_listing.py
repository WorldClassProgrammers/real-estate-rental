from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, CustomUser, Unit, CondoImages,UnitImages


class TestCondoListingView(TestCase):

    def test_condo_listing_with_one_condo(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        response = self.client.get(reverse('estate:condo_listing'))
        self.assertContains(response, condo.name)

    def test_condo_listing_with_many_condo(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        condo2 = Condo.objects.create(name="Condo2", description="This is not a real condo.", number_of_floors=20,
                                     juristic_persons_number='21764-5432', common_fee_account='67890')
        condoimage2 = CondoImages.objects.create(condo=condo2, image='condo.png')
        condoimage2.save()
        condo2.save()
        response = self.client.get(reverse('estate:condo_listing'))
        self.assertContains(response, condo.name)
        self.assertNotContains(response, condo2.name)
