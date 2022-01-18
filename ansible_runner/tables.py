"""Tables for ansible_runner."""

import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ButtonsColumn, ToggleColumn

from ansible_runner import models


class AnsibleProjectsTable(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(models.AnsibleProjects, buttons=("edit", "delete"), pk_field="slug")

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.AnsibleProjects
        fields = (
            "pk",
            "name",
            "description",
        )
