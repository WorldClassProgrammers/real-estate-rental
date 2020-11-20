from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, Owner, Room


class TestIndexView(TestCase):

    def test_no_condo(self):
        response = self.client.get(reverse('estate:index'))
        self.assertContains(response, "No condo available.")

    def test_have_condo(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17)
        condo.save()
        response = self.client.get(reverse('estate:index'))
        self.assertContains(response, condo.name)
        self.assertContains(response, condo.number_of_floors)
