from django.urls import reverse
from oc_lettings_site.tests.base_tests import BaseTestSetup


class ProfilesViewsTests(BaseTestSetup):

    def test_profiles_index_view(self):
        path = reverse("profiles:index")

        response = self.client.get(path)

        content = response.content.decode()
        expected_content = "JD"

        self.assertInHTML(expected_content, content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profile_view(self):
        path = reverse("profiles:profile", kwargs={"username": "JD"})
        response = self.client.get(path)

        content = response.content.decode()
        expected_content = "<p><strong>Email :</strong> johndoe@email.com</p>"
        self.assertInHTML(expected_content, content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
