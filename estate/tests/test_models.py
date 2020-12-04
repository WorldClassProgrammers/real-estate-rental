from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, CustomUser, Unit


class TestCondoModel(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user("John", "john@gmail.com", "12345", role=1)
        self.user.first_name = 'John'
        self.user.last_name = "Davidson"
        self.user.save()

    def test_condo_with_room(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17)
        condo.save()
        unit = Unit.objects.create(condo=condo, title='unit 1', description='This is not a real unit.', owner=self.user)
        unit.save()
        unit2 = Unit.objects.create(condo=condo, title='unit 2', description='This is not a real unit.', owner=self.user)
        unit2.save()
        self.assertEqual(condo.get_all_register_unit(), 2)

    def test_condo_with_no_room(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17)
        condo.save()
        self.assertEqual(condo.get_all_register_unit(), 0)

    def test_condo_with_room_not_available(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17)
        condo.save()
        unit = Unit.objects.create(condo=condo, title='unit 1', description='This is not a real unit.', owner=self.user)
        unit.save()
        room2 = Unit.objects.create(condo=condo, title='unit 2', description='This is not a real unit.', owner=self.user, still_on_contract=True)
        room2.save()
        self.assertEqual(condo.get_available_units(), 1)

    def test_condo_with_room_no_room_available(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17)
        condo.save()
        unit = Unit.objects.create(condo=condo, title='unit 1', description='This is not a real unit.', owner=self.user, still_on_contract=True)
        unit.save()
        unit2 = Unit.objects.create(condo=condo, title='unit 2', description='This is not a real unit.', owner=self.user, still_on_contract=True)
        unit2.save()
        self.assertEqual(condo.get_available_units(), 0)
