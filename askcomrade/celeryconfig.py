from config import config
from celery import Celery
celery_app = Celery('tasks',
                    backend=config.celery_backend_uri,
                    broker=config.celery_broker_uri)
celery_app.conf.update(
    CELERY_IMPORTS=(
        'app.module_a.tasks',   # we're not including our tasks here as
        'app.module_b.tasks',   # our tasks are in other files listed here
    )
)