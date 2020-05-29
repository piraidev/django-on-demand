
from django.apps import apps
from django.core.checks import Error

REQUIRED_INSTALLED_APPS = [
    'rest_framework'
]


def required_installed_apps(app_configs, **kwargs):
    errors = []
    for app in REQUIRED_INSTALLED_APPS:
        if not apps.is_installed(app):
            errors.append(
                Error(f'{app} is required in INSTALLED_APPS')
            )
    return errors
