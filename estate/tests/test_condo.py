from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, Unit, CondoImages, UnitImages, CustomUser


class TestCondoView(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user("John", "john@gmail.com", "12345", role=1)
        self.user.first_name = 'John'
        self.user.last_name = "Davidson"
        self.user.save()

    def test_add_condo(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        response = self.client.get(reverse('estate:condo', args=(condo.id,)))
        self.assertContains(response, condo.name)
        self.assertEqual(condo.number_of_floors, 17)

    def test_add_room_in_condo(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        unit = Unit.objects.create(condo=condo, title='room 1', description='This is not a real room.', owner=self.user)
        unitimage = UnitImages.objects.create(unit=unit, image='room.png')
        unitimage.save()
        unit.save()
        response = self.client.get(reverse('estate:condo', args=(condo.id,)))
        self.assertContains(response, unit.title)

    def test_condo_not_exist(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        response = self.client.get(reverse('estate:condo', args=(condo.id+1,)))
        self.assertEqual(response.status_code, 404)

