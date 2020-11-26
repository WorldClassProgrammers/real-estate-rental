from django.test import TestCase
from django.urls import reverse
from estate.models import Condo, Unit, CondoImages,UnitImages, CustomUser


class TestUploadIndexView(TestCase):

    def test_upload_index_without_login(self):
        response = self.client.get(reverse('estate:upload_index'))
        self.assertEqual(response.status_code, 302)

    def test_upload_when_user_is_visitor(self):
        user = CustomUser.objects.create_user("John", "john@gmail.com", "12345", role=1)
        user.first_name = 'John'
        user.last_name = "Davidson"
        user.save()
        self.client.login(username="John", password="12345")
        response = self.client.get(reverse('estate:upload_index'))
        self.assertRedirects(response, reverse('estate:index'))

    def test_upload_when_user_is_owner(self):
        user = CustomUser.objects.create_user("John", "john@gmail.com", "12345", role=2)
        user.first_name = 'John'
        user.last_name = "Davidson"
        user.save()
        self.client.login(username="John", password="12345")
        response = self.client.get(reverse('estate:upload_index'))
        self.assertEqual(response.status_code, 200)
