"""Create fixtures for tests."""
from ansible_runner.models import AnsibleProjects


def create_ansibleprojects():
    """Fixture to create necessary number of AnsibleProjects for tests."""
    AnsibleProjects.objects.create(name="Test One", slug="test-one")
    AnsibleProjects.objects.create(name="Test Two", slug="test-two")
    AnsibleProjects.objects.create(name="Test Three", slug="test-three")
