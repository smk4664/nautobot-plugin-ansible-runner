"""Forms for ansible_runner."""
from django import forms
from nautobot.utilities.forms import (
    BootstrapMixin,
    BulkEditForm,
    SlugField,
)

from ansible_runner import models


class AnsibleProjectsForm(BootstrapMixin, forms.ModelForm):
    """AnsibleProjects creation/edit form."""

    slug = SlugField()

    class Meta:
        """Meta attributes."""

        model = models.AnsibleProjects
        fields = [
            "name",
            "slug",
            "description",
        ]


class AnsibleProjectsBulkEditForm(BootstrapMixin, BulkEditForm):
    """AnsibleProjects bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.AnsibleProjects.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class AnsibleProjectsFilterForm(BootstrapMixin, forms.ModelForm):
    """Filter form to filter searches."""

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
    slug = forms.CharField(required=False, label="Slug")

    class Meta:
        """Meta attributes."""

        model = models.AnsibleProjects
        # Define the fields above for ordering and widget purposes
        fields = [
            "q",
            "name",
            "slug",
            "description",
        ]
