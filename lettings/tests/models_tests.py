from oc_lettings_site.tests.base_tests import BaseTestSetup


class LettingsModelsTests(BaseTestSetup):

    def test_address_model(self):
        expected_value = "1 test street"

        assert str(self.test_address) == expected_value

    def test_letting_model(self):
        expected_value = "test_letting"

        assert str(self.test_letting) == expected_value
