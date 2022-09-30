from django.apps import AppConfig


class EventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PlayGroundEvent'

    def ready(self):
        from PlayGroundEvent import signals
