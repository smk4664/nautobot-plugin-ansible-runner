"""API serializers for ansible_runner."""
from rest_framework import serializers

from nautobot.core.api.serializers import ValidatedModelSerializer

from ansible_runner import models

from . import nested_serializers  # noqa: F401, pylint: disable=unused-import


class AnsibleProjectsSerializer(ValidatedModelSerializer):
    """AnsibleProjects Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:ansible_runner-api:ansibleprojects-detail")

    class Meta:
        """Meta attributes."""

        model = models.AnsibleProjects
        fields = "__all__"
