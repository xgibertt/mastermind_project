from django.contrib.auth.models import User
from django.test import TestCase
from faker import Faker
from faker.providers import BaseProvider
from rest_framework.test import APIClient


class FakerProvider(BaseProvider):
    def code(self):
        return self.random_sample(elements=('R', 'B', 'G', 'Y'), length=4)

    def serialized_code(self):
        return self.random_sample(elements=('RED', 'BLUE', 'GREEN', 'YELLOW'), length=4)

    def peg(self):
        return self.random_element(elements=(0, 1, 2, 3, 4))

    def n_rounds(self):
        return self.random_element(elements=(12, 10, 8, 6))

    def boolean(self):
        return self.random_element(elements=(True, False))


class BaseTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(FakerProvider)

        self.client = APIClient()

        self.user_username = u"test"
        self.user_password = u"test$"
        self.user_mail = u"test@test.com"

        self.superuser_username = u"testadmin"
        self.superuser_password = u"testadmin$"
        self.superuser_mail = u"testadmin@testadmin.com"

        User.objects.create_user(self.user_username,
                                 self.user_mail,
                                 self.user_password)
        User.objects.create_superuser(self.superuser_username,
                                      self.superuser_mail,
                                      self.superuser_password)

    def _user_login(self):
        self.client.login(username=self.user_username, password=self.user_password)

    def _superuser_login(self):
        self.client.login(username=self.superuser_username, password=self.superuser_password)

    def _logout(self):
        self.client.logout()

    def _get_id_by_url(self, url):
        count = len(url.split("/"))
        return int(url.split("/")[count - 2])

