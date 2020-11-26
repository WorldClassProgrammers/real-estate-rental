from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, CustomUser, Unit, CondoImages,UnitImages


class TestRoomView(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user("John", "john@gmail.com", "12345", role=1)
        self.user.first_name = 'John'
        self.user.last_name = "Davidson"
        self.user.save()

    def test_room_not_exist(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        unit = Unit.objects.create(condo=condo, title='unit 1', description='This is not a real unit.', owner=self.user)
        unitimage = UnitImages.objects.create(unit=unit, image='unit.png')
        unitimage.save()
        unit.save()
        response = self.client.get(reverse('estate:unit', args=(unit.id+1,)))
        self.assertEqual(response.status_code, 404)

    def test_add_room(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        unit = Unit.objects.create(condo=condo, title='unit 2', description='This is not a real unit.', owner=self.user)
        unitimage = UnitImages.objects.create(unit=unit, image='unit.png')
        unitimage.save()
        unit.save()
        response = self.client.get(reverse('estate:unit', args=(unit.id,)))
        self.assertContains(response, unit.title)
