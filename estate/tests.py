from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, Owner, Room


class TestIndexView(TestCase):

    def test_no_condo(self):
        response = self.client.get(reverse('estate:index'))
        self.assertContains(response, "No room are available.")


class TestCondoView(TestCase):

    def test_add_condo(self):
        condo = Condo.objects.create(condo_name="Condo", condo_description="This is not a real condo.", number_of_floors=17)
        condo.save()
        response = self.client.get(reverse('estate:condo', args=[condo.id]))
        self.assertContains(response, condo.condo_name)
        self.assertContains(response, condo.condo_description)
        self.assertEqual(condo.number_of_floors, 17)

    def test_condo_with_no_room(self):
        condo = Condo.objects.create(condo_name="Condo", condo_description="This is not a real condo.", number_of_floors=10)
        condo.save()
        response = self.client.get(reverse('estate:condo', args=[condo.id]))
        self.assertContains(response, "No room are available")

    def test_add_room_in_condo(self):
        condo = Condo.objects.create(condo_name="Condo", condo_description="This is not a real condo.", number_of_floors=10)
        condo.save()
        owner = Owner.objects.create(owner_name='Johnson', owner_email='johnson@gmail.com', owner_line_id='johnson1234', owner_phone_number='0101010')
        owner.save()
        room = Room.objects.create(condo_name=condo, room_title='room 1', room_description='This is not a real room.', owner_name=owner)
        room.save()
        response = self.client.get(reverse('estate:condo', args=[condo.id]))
        self.assertContains(response, room.room_title)

    def test_condo_not_exist(self):
        condo = Condo.objects.create(condo_name="Condo", condo_description="This is not a real condo.", number_of_floors=10)
        condo.save()
        response = self.client.get(reverse('estate:condo', args=[condo.id+1]))
        self.assertEqual(response.status_code, 404)


class TestRoomView(TestCase):

    def test_room_not_exist(self):
        condo = Condo.objects.create(condo_name="Condo", condo_description="This is not a real condo.", number_of_floors=10)
        condo.save()
        owner = Owner.objects.create(owner_name='Johnson', owner_email='johnson@gmail.com', owner_line_id='johnson1234', owner_phone_number='0101010')
        owner.save()
        room = Room.objects.create(condo_name=condo, room_title='room 1', room_description='This is not a real room.', owner_name=owner)
        room.save()
        response = self.client.get(reverse('estate:room', args=[room.id+1]))
        self.assertEqual(response.status_code, 404)

    def test_add_room(self):
        condo = Condo.objects.create(condo_name="Condo", condo_description="This is not a real condo.", number_of_floors=10)
        condo.save()
        owner = Owner.objects.create(owner_name='Johnson', owner_email='johnson@gmail.com', owner_line_id='johnson1234', owner_phone_number='0101010')
        owner.save()
        room = Room.objects.create(condo_name=condo, room_title='room 1', room_description='This is not a real room.', owner_name=owner)
        room.save()
        response = self.client.get(reverse('estate:room', args=[room.id]))
        self.assertContains(response, room.room_title)
        self.assertContains(response, room.room_description)
