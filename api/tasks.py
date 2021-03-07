from celery import Celery, shared_task
from celery.schedules import crontab
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from alpha_vantage.foreignexchange import ForeignExchange
from .models import BTC
import os
from btc_app.settings import ALPHA_VANTAGE_KEY


@shared_task()
def fetch_btc_every_hour(now = False):
    try:
        if now:
            fetch_from_alpha_vantage()
        else:
            fetch_from_alpha_vantage()
    except Exception as e:
        return "Something went wrong!"


def fill_db_table(data: dict):
    try:
        price = data['8. Bid Price']
        exchange_rate = data['5. Exchange Rate']
        updated_at = data['6. Last Refreshed']
        BTC.objects.create(price=price,exchange_rate=exchange_rate,updated_at=updated_at)
        print("Saved perfectly!")
    except Exception as e:
        print(f"error is in fill_db_table{e}")


def fetch_from_alpha_vantage():
    try:
        cc = ForeignExchange(key=ALPHA_VANTAGE_KEY)
        data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
        fill_db_table(data)
    except Exception as e:
        print(f"The error is in run_every_hour => {e}")


#schedual to run every 30 seconds
schedual, created = IntervalSchedule.objects.get_or_create(
    every= 1,
    period= IntervalSchedule.HOURS
)


PeriodicTask.objects.get_or_create(
    interval = schedual,
    name = "Fetch BTC Every hour",
    task = 'api.tasks.fetch_btc_every_hour'
)





# def stop_task(task_id):
#     print("Before revoking")
#     app.control.revoke(task_id, Terminate= True)
#     print("After revoking")



