from django.apps import AppConfig


class CourierMgtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courier_mgt'

    def ready(self):
        import courier_mgt.signals
