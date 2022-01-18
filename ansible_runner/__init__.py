"""Plugin declaration for ansible_runner."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class AnsibleRunnerConfig(PluginConfig):
    """Plugin configuration for the ansible_runner plugin."""

    name = "ansible_runner"
    verbose_name = "Ansible Runner"
    version = __version__
    author = "Network to Code, LLC"
    description = "Ansible Runner."
    base_url = "ansible-runner"
    required_settings = []
    min_version = "1.2.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = AnsibleRunnerConfig  # pylint:disable=invalid-name
