from django.urls import reverse
from .base_tests import BaseTestSetup


class BaseViews(BaseTestSetup):

    def test_index_view(self):
        path = reverse("index")

        response = self.client.get(path)

        content = response.content.decode()
        expected_content = (
            '<h1 class="page-header-ui-title mb-3 display-6">'
            "Welcome to Holiday Homes</h1>"
        )

        self.assertInHTML(expected_content, content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_404_view(self):
        path = "/notvalidpath"

        response = self.client.get(path)

        content = response.content.decode()
        expected_content = "<p>The page you are looking for doesn't exists.</p>"

        self.assertInHTML(expected_content, content)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
