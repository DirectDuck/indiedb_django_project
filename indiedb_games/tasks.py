from celery.task.schedules import crontab
from celery.decorators import periodic_task

from . import parser

@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)
def parser_update_db():  
    parser.update_db()