from django.urls import reverse, resolve
from oc_lettings_site.tests.base_tests import BaseTestSetup


class UrlTests(BaseTestSetup):

    def test_index_url(self):
        path = reverse("profiles:index")

        assert path == "/profiles/"
        assert resolve(path).view_name == "profiles:index"

    def test_profile_url(self):

        path = reverse(
            "profiles:profile", kwargs={"username": self.test_profile.user.username}
        )

        assert path == "/profiles/JD/"
        assert resolve(path).view_name == "profiles:profile"
