"""Django API urlpatterns declaration for ansible_runner plugin."""

from nautobot.core.api import OrderedDefaultRouter

from ansible_runner.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("ansibleprojects", views.AnsibleProjectsViewSet)


app_name = "ansible_runner-api"
urlpatterns = router.urls
