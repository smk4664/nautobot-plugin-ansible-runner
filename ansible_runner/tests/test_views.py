"""Unit tests for views."""
from nautobot.utilities.testing import ViewTestCases

from ansible_runner import models
from ansible_runner.tests import fixtures


class AnsibleProjectsViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the AnsibleProjects views."""

    model = models.AnsibleProjects
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "slug": "test-1",
        "description": "Initial model",
    }

    @classmethod
    def setUpTestData(cls):
        fixtures.create_ansibleprojects()

    def test_bulk_import_objects_with_constrained_permission(self):
        pass

    def test_bulk_import_objects_with_permission(self):
        pass

    def test_bulk_import_objects_without_permission(self):
        pass
