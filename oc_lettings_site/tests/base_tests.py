from django.test import Client, TestCase
from profiles.models import Profile
from django.contrib.auth.models import User
from lettings.models import Address, Letting

class BaseTestSetup(TestCase):


    def setUp(self):

        self.client = Client()
        self.test_user = User.objects.create(password="123456",
                           username="JD",
                           first_name="John",
                           last_name="Doe",
                           email="johndoe@email.com"
                           )

        self.test_profile = Profile.objects.create(user= self.test_user,
                                        favorite_city="Paris")
        self.test_address = Address.objects.create(
            number=1,
            street="test street",
            city='paris',
            state='France',
            zip_code ="75001",
            country_iso_code="FRA",
        )
        
        self.test_letting = Letting.objects.create(title="test_letting",
                                                   address=self.test_address)
        

        return super().setUp()