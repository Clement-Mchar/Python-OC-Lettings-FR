from django.urls import reverse, resolve
from oc_lettings_site.tests.base_tests import BaseTestSetup

class ProfilesModelTest(BaseTestSetup):

    def test_profile_mode(self):
        expected_value = "JD"
        assert str(self.test_profile) == expected_value