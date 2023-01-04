"""{{ cookiecutter.project_short_description }}."""

from plugin import InvenTreePlugin
# from plugin.mixins import SettingsMixin
# from django.utils.translation import gettext_lazy as _


class {{ cookiecutter.project_plugin_name }}(InvenTreePlugin):
    """{{ cookiecutter.project_short_description }}."""

    NAME = '{{ cookiecutter.project_plugin_name }}'
    SLUG = '{{ cookiecutter.project_slug }}'
    TITLE = "{{ cookiecutter.project_name }}"

    def your_function_here(self):
        """Do something."""
        pass
