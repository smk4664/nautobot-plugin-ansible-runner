"""Unit tests for ansible_runner."""
from nautobot.utilities.testing import APIViewTestCases

from ansible_runner import models
from ansible_runner.tests import fixtures


class AnsibleProjectsAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for AnsibleProjects."""

    model = models.AnsibleProjects
    create_data = [
        {
            "name": "Test Model 1",
            "slug": "test-model-1",
        },
        {
            "name": "Test Model 2",
            "slug": "test-model-2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}
    brief_fields = ["created", "description", "display", "id", "last_updated", "name", "slug", "url"]

    @classmethod
    def setUpTestData(cls):
        fixtures.create_ansibleprojects()
