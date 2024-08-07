from django.urls import reverse
from oc_lettings_site.tests.base_tests import BaseTestSetup


class ViewsTests(BaseTestSetup):

    def test_lettings_index_view(self):
        path = reverse("lettings:index")

        response = self.client.get(path)

        content = response.content.decode()
        expected_content = "test_letting"

        self.assertInHTML(expected_content, content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_letting_view(self):
        path = reverse("lettings:letting", kwargs={"letting_id": 1})
        response = self.client.get(path)

        content = response.content.decode()
        expected_content = "<p> 1 test street </p>"
        self.assertInHTML(expected_content, content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
