from django.urls import reverse, resolve
from oc_lettings_site.tests.base_tests import BaseTestSetup


class UrlTests(BaseTestSetup):

    def test_index_url(self):
        path = reverse("lettings:index")

        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings:index"

    def test_letting_url(self):

        path = reverse("lettings:letting", kwargs={"letting_id": self.test_letting.id})

        assert path == "/lettings/1/"
        assert resolve(path).view_name == "lettings:letting"
