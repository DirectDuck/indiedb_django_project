from __future__ import absolute_import, unicode_literals

from celery.task import periodic_task
from celery.schedules import crontab

from . import parser

@periodic_task(run_every=(crontab(minute='*/1')), name='some_task')
def parser_update_db():  
    parser.update_db() 