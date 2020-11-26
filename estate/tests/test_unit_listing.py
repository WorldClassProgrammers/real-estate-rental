from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, CustomUser, Unit, CondoImages,UnitImages


class TestUnitListingView(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user("John", "john@gmail.com", "12345", role=1)
        self.user.first_name = 'John'
        self.user.last_name = "Davidson"
        self.user.save()

    def test_unit_listing_with_one_unit(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        unit = Unit.objects.create(condo=condo, title='unit 1', description='This is not a real unit.', owner=self.user)
        unitimage = UnitImages.objects.create(unit=unit, image='unit.png')
        unitimage.save()
        unit.save()
        response = self.client.get(reverse('estate:unit_listing'))
        self.assertContains(response, unit.title)

    def test_unit_listing_with_many_unit(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        unit = Unit.objects.create(condo=condo, title='unit 1', description='This is not a real unit.', owner=self.user)
        unitimage = UnitImages.objects.create(unit=unit, image='unit.png')
        unitimage.save()
        unit.save()
        unit2 = Unit.objects.create(condo=condo, title='unit 2', description='This is not a real unit.', owner=self.user)
        unitimage2 = UnitImages.objects.create(unit=unit2, image='unit.png')
        unitimage2.save()
        unit2.save()
        response = self.client.get(reverse('estate:unit_listing'))
        self.assertContains(response, unit.title)
        self.assertContains(response, unit2.title)
