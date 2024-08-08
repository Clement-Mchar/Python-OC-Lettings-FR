from django.urls import reverse
from oc_lettings_site.tests.base_tests import BaseTestSetup
from unittest.mock import patch

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

    @patch('lettings.views.letting')
    def test_capture_exception(self, mock_capture_exception):
        path = reverse("lettings:letting", kwargs={"letting_id": 2})
        with self.assertRaises(UnboundLocalError):
            response = self.client.get(path)
            self.assertEqual(response.status_code, 500)
            mock_capture_exception.assert_called_once()
            exception_captured = mock_capture_exception.call_args[0][0]
            assert isinstance(exception_captured, UnboundLocalError)
            assert str(exception_captured) == "cannot access local variable 'context' where it is not associated with a value"