from django.test import TestCase

from faker import Faker
from faker.providers import BaseProvider


class FakerProvider(BaseProvider):
    def code(self):
        return self.random_sample(elements=('R', 'B', 'G', 'Y'), length=4)

    def peg(self):
        return self.random_element(elements=(0, 1, 2, 3, 4))

    def boolean(self):
        return self.random_element(elements=(True, False))


class BaseTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(FakerProvider)
