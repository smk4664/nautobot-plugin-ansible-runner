"""Test AnsibleProjects."""

from django.test import TestCase

from ansible_runner import models


class TestAnsibleProjects(TestCase):
    """Test AnsibleProjects."""

    def test_create_ansibleprojects_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        ansibleprojects = models.AnsibleProjects.objects.create(name="Development", slug="development")
        self.assertEqual(ansibleprojects.name, "Development")
        self.assertEqual(ansibleprojects.description, "")
        self.assertEqual(str(ansibleprojects), "Development")
        self.assertEqual(ansibleprojects.slug, "development")

    def test_create_ansibleprojects_all_fields_success(self):
        """Create AnsibleProjects with all fields."""
        ansibleprojects = models.AnsibleProjects.objects.create(
            name="Development", slug="development", description="Development Test"
        )
        self.assertEqual(ansibleprojects.name, "Development")
        self.assertEqual(ansibleprojects.slug, "development")
        self.assertEqual(ansibleprojects.description, "Development Test")
