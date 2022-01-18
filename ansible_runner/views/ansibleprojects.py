"""Views for AnsibleProjects."""

from nautobot.core.views import generic

from ansible_runner import filters, forms, models, tables


class AnsibleProjectsListView(generic.ObjectListView):
    """List view."""

    queryset = models.AnsibleProjects.objects.all()
    # These aren't needed for simple models, but we can always add
    # this search functionality.
    filterset = filters.AnsibleProjectsFilterSet
    filterset_form = forms.AnsibleProjectsFilterForm
    table = tables.AnsibleProjectsTable
    action_buttons = ("add", "export")


class AnsibleProjectsView(generic.ObjectView):
    """Detail view."""

    queryset = models.AnsibleProjects.objects.all()


class AnsibleProjectsCreateView(generic.ObjectEditView):
    """Create view."""

    model = models.AnsibleProjects
    queryset = models.AnsibleProjects.objects.all()
    model_form = forms.AnsibleProjectsForm


class AnsibleProjectsDeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.AnsibleProjects
    queryset = models.AnsibleProjects.objects.all()


class AnsibleProjectsEditView(generic.ObjectEditView):
    """Edit view."""

    model = models.AnsibleProjects
    queryset = models.AnsibleProjects.objects.all()
    model_form = forms.AnsibleProjectsForm


class AnsibleProjectsBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more AnsibleProjects records."""

    queryset = models.AnsibleProjects.objects.all()
    table = tables.AnsibleProjectsTable


class AnsibleProjectsBulkEditView(generic.BulkEditView):
    """View for editing one or more AnsibleProjects records."""

    queryset = models.AnsibleProjects.objects.all()
    table = tables.AnsibleProjectsTable
    form = forms.AnsibleProjectsBulkEditForm
