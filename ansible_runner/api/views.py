"""API views for ansible_runner."""

from nautobot.core.api.views import ModelViewSet

from ansible_runner import filters, models

from ansible_runner.api import serializers


class AnsibleProjectsViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    """AnsibleProjects viewset."""

    queryset = models.AnsibleProjects.objects.all()
    serializer_class = serializers.AnsibleProjectsSerializer
    filterset_class = filters.AnsibleProjectsFilterSet
