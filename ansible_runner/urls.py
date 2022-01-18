"""Django urlpatterns declaration for ansible_runner plugin."""
from django.urls import path
from nautobot.extras.views import ObjectChangeLogView

from ansible_runner import models
from ansible_runner.views import ansibleprojects

urlpatterns = [
    # AnsibleProjects URLs
    path("ansibleprojects/", ansibleprojects.AnsibleProjectsListView.as_view(), name="ansibleprojects_list"),
    # Order is important for these URLs to work (add/delete/edit) to be before any that require uuid/slug
    path("ansibleprojects/add/", ansibleprojects.AnsibleProjectsCreateView.as_view(), name="ansibleprojects_add"),
    path("ansibleprojects/delete/", ansibleprojects.AnsibleProjectsBulkDeleteView.as_view(), name="ansibleprojects_bulk_delete"),
    path("ansibleprojects/edit/", ansibleprojects.AnsibleProjectsBulkEditView.as_view(), name="ansibleprojects_bulk_edit"),
    path("ansibleprojects/<slug:slug>/", ansibleprojects.AnsibleProjectsView.as_view(), name="ansibleprojects"),
    path("ansibleprojects/<slug:slug>/delete/", ansibleprojects.AnsibleProjectsDeleteView.as_view(), name="ansibleprojects_delete"),
    path("ansibleprojects/<slug:slug>/edit/", ansibleprojects.AnsibleProjectsEditView.as_view(), name="ansibleprojects_edit"),
    path(
        "ansibleprojects/<slug:slug>/changelog/",
        ObjectChangeLogView.as_view(),
        name="ansibleprojects_changelog",
        kwargs={"model": models.AnsibleProjects},
    ),
]
