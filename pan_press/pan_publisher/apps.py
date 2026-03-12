from django.apps import AppConfig


class PanPublisherConfig(AppConfig):
    name = 'pan_publisher'

    # Configuración de la tarea periódica de escanear 'content/',
    # script definido en tasks.py.
    def ready(self):
        SCAN_PERIOD = 10
        
        from apscheduler.schedulers.background import BackgroundScheduler
        from django_aapscheduler.jobstores import DjangoJobStore
        from .tasks import scan_articles

        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(
            scan_articles,
            "interval",
            minutes=SCAN_PERIOD,
            id="scan_articles",
            replace_existing=True,
        )
        scheduler.start()
