from django.apps import AppConfig


class ContentConfig(AppConfig):
    name = 'Content'

    def ready(self):
        import Content.signals
