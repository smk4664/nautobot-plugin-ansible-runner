"""Menu items."""

from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:ansible_runner:ansibleprojects_list",
        link_text="Ansible Runner",
        buttons=(
            PluginMenuButton(
                link="plugins:ansible_runner:ansibleprojects_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["ansible_runner.add_ansibleprojects"],
            ),
        ),
    ),
)
