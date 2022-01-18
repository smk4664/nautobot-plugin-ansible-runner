"""Test AnsibleProjects Filter."""
from django.test import TestCase
from ansible_runner import filters
from ansible_runner import models
from ansible_runner.tests import fixtures


class AnsibleProjectsFilterTestCase(TestCase):
    """AnsibleProjects Filter Test Case."""

    queryset = models.AnsibleProjects.objects.all()
    filterset = filters.AnsibleProjectsFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for AnsibleProjects Model."""
        fixtures.create_ansibleprojects()

    def test_q_search_name(self):
        """Test using Q search with name of AnsibleProjects."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_search_slug(self):
        """Test using Q search with slug of AnsibleProjects."""
        params = {"q": "test-one"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for AnsibleProjects."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
