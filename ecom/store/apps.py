from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'store'

    def ready(self):
        # Do not access models or the database here directly
        pass
