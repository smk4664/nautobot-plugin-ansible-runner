"""API nested serializers for ansible_runner."""
from rest_framework import serializers

from nautobot.core.api import WritableNestedSerializer

from ansible_runner import models


class AnsibleProjectsNestedSerializer(WritableNestedSerializer):
    """AnsibleProjects Nested Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:ansible_runner-api:ansibleprojects-detail")

    class Meta:
        """Meta attributes."""

        model = models.AnsibleProjects
        fields = "__all__"
