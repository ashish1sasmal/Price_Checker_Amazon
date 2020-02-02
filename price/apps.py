from django.apps import AppConfig


class PriceConfig(AppConfig):
    name = 'price'

    def ready(self):
        from . import views
        views.start()
