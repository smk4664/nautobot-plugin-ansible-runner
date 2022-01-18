"""Filtering for ansible_runner."""

from nautobot.utilities.filters import BaseFilterSet, NameSlugSearchFilterSet

from ansible_runner import models


class AnsibleProjectsFilterSet(BaseFilterSet, NameSlugSearchFilterSet):
    """Filter for AnsibleProjects."""

    class Meta:
        """Meta attributes for filter."""

        model = models.AnsibleProjects

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "slug", "description"]
