from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, Owner, Room, CondoImages,RoomImages


class TestRoomView(TestCase):

    def test_room_not_exist(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        owner = Owner.objects.create(name='Johnson', email='johnson@gmail.com', line_id='johnson1234', phone_number='0101010')
        owner.save()
        room = Room.objects.create(condo=condo, title='room 1', description='This is not a real room.', owner=owner)
        roomimage = RoomImages.objects.create(room=room, image='room.png')
        roomimage.save()
        room.save()
        response = self.client.get(reverse('estate:room', args=(room.id+1,)))
        self.assertEqual(response.status_code, 404)

    def test_add_room(self):
        condo = Condo.objects.create(name="Condo", description="This is not a real condo.", number_of_floors=17,
                                     juristic_persons_number='21754-5432', common_fee_account='12345')
        condoimage = CondoImages.objects.create(condo=condo, image='condo.png')
        condoimage.save()
        condo.save()
        owner = Owner.objects.create(name='Johnson', email='johnson@gmail.com', line_id='johnson1234', phone_number='0101010')
        owner.save()
        room = Room.objects.create(condo=condo, title='room 2', description='This is not a real room.', owner=owner)
        roomimage = RoomImages.objects.create(room=room, image='room.png')
        roomimage.save()
        room.save()
        response = self.client.get(reverse('estate:room', args=(room.id,)))
        self.assertContains(response, room.title)
