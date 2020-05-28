default_app_config = 'on_demand.apps.OnDemandConfig'

# to be added into INSTALLED_APPS later
CORE_APPS = [
    "rest_framework"  # external apps
]


def get_core_apps():
    return CORE_APPS
