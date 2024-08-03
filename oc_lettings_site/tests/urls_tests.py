from django.urls import reverse, resolve
from .base_tests import BaseTestSetup

class UrlsTests(BaseTestSetup):

    def test_index_url(self):
        path = reverse('index')

        assert path == "/"
        assert resolve(path).view_name == "index"

    def test_lettings_urls_inclusions(self):
        path = reverse("lettings:index")
        assert path == "/lettings/"
        assert resolve(path).namespace == "lettings"
        
    def test_profiles_urls_inclusions(self):
        path = reverse("profiles:index")
        assert path == "/profiles/"
        assert resolve(path).namespace == "profiles"
