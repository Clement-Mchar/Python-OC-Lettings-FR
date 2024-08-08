from django.urls import reverse
from oc_lettings_site.tests.base_tests import BaseTestSetup
from unittest.mock import patch

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

    @patch('profiles.views.profile')
    def test_capture_exception(self, mock_capture_exception):
        path = reverse("profiles:profile", kwargs={"username": "Serge"})
        with self.assertRaises(UnboundLocalError):
            response = self.client.get(path)
            self.assertEqual(response.status_code, 500)
            mock_capture_exception.assert_called_once()
            exception_captured = mock_capture_exception.call_args[0][0]
            assert isinstance(exception_captured, UnboundLocalError)
            assert str(exception_captured) == "cannot access local variable 'context' where it is not associated with a value"