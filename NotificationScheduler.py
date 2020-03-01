import datetime
import multiprocessing
import schedule
import time
from threading import Lock

from Service import Service
from SQLRepository import SQLRepository

class NotificationScheduler:
    
    def execute(self):
        sql = SQLRepository()
        tasks = sql.collectAllonSchedule()
        service = Service()
        for task in tasks:
            service.sendPushNotfication(task[0], task[1])
            sql.updateSchedule(task.pending_id)
