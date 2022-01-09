from django.apps import AppConfig


class InspectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inspection'

    def ready(self):
        from statusupdater import updater
        updater.start()