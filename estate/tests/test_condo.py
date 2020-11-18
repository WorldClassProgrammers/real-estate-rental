from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, Owner, Room


class TestCondoView(TestCase):

    def test_add_condo(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condo.save()
        # response = self.client.get(reverse('estate:condo', args=(condo.id,)))
        # # self.assertContains(response, condo.name)
        # # self.assertEqual(condo.number_of_floors, 17)

    def test_add_room_in_condo(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=10)
        condo.save()
        owner = Owner.objects.create(name='Johnson', email='johnson@gmail.com', line_id='johnson1234', phone_number='0101010')
        owner.save()
        room = Room.objects.create(condo=condo, title='room 1', description='This is not a real room.', owner=owner)
        room.save()
        response = self.client.get(reverse('estate:condo', args=(condo.id,)))
        self.assertContains(response, room.title)

    def test_condo_not_exist(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=10)
        condo.save()
        response = self.client.get(reverse('estate:condo', args=(condo.id+1,)))
        self.assertEqual(response.status_code, 404)
