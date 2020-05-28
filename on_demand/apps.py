from django.apps import AppConfig


class OnDemandConfig(AppConfig):
    name = 'on_demand'

    def ready(self):
        import on_demand.receivers
