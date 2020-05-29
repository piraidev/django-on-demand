from django.apps import AppConfig
from django.core.checks import register

from . import settings_validation


class OnDemandConfig(AppConfig):
    name = 'on_demand'

    def ready(self):
        import on_demand.receivers
        register(
            settings_validation.required_installed_apps
        )
