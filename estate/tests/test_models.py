from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, Owner, Unit


class TestCondoModel(TestCase):

    def test_condo_with_room(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17)
        condo.save()
        owner = Owner.objects.create(name='Johnson', email='johnson@gmail.com', line_id='johnson1234', phone_number='0101010')
        owner.save()
        room = Unit.objects.create(condo=condo, title='room 1', description='This is not a real room.', owner=owner)
        room.save()
        room2 = Unit.objects.create(condo=condo, title='room 2', description='This is not a real room.', owner=owner)
        room2.save()
        self.assertEqual(condo.get_all_register_unit(), 2)

    def test_condo_with_no_room(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17)
        condo.save()
        self.assertEqual(condo.get_all_register_unit(), 0)

    def test_condo_with_room_not_available(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17)
        condo.save()
        owner = Owner.objects.create(name='Johnson', email='johnson@gmail.com', line_id='johnson1234', phone_number='0101010')
        owner.save()
        room = Unit.objects.create(condo=condo, title='room 1', description='This is not a real room.', owner=owner)
        room.save()
        room2 = Unit.objects.create(condo=condo, title='room 2', description='This is not a real room.', owner=owner, still_on_contract=True)
        room2.save()
        self.assertEqual(condo.get_available_units(), 1)

    def test_condo_with_room_no_room_available(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17)
        condo.save()
        owner = Owner.objects.create(name='Johnson', email='johnson@gmail.com', line_id='johnson1234', phone_number='0101010')
        owner.save()
        room = Unit.objects.create(condo=condo, title='room 1', description='This is not a real room.', owner=owner, still_on_contract=True)
        room.save()
        room2 = Unit.objects.create(condo=condo, title='room 2', description='This is not a real room.', owner=owner, still_on_contract=True)
        room2.save()
        self.assertEqual(condo.get_available_units(), 0)
