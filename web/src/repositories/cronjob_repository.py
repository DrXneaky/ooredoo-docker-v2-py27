
from ..entities.cron_job import CronJob
import datetime
from sqlalchemy_pagination import paginate
from cron_descriptor import get_description

def generate_cron_job(session, cronjob_to_save, status, nextRun):

  if cronjob_to_save["creationDate"] is None:
    cronjob_to_save["creationDate"] = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S") 
  nextRun = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
  #expression = cronjob_to_save["minute"]+" "+ cronjob_to_save["hour"]+" "+cronjob_to_save["day"]+" "+cronjob_to_save["month"]+" "+cronjob_to_save["weekDay"]
  expression = cronjob_to_save["expression"]
  schedule = get_description(expression) 
  cron_job = CronJob(
    datetime.datetime.now(),
    cronjob_to_save["command"],
    cronjob_to_save["type"],
    schedule,
    expression,
    cronjob_to_save["lastRun"],
    status,
    nextRun,
    )

  session.add(cron_job)
  session.flush()
  print (cron_job.id)
  return cron_job



def get_cron_jobs(session, page, size):
  pagination = paginate(session.query(CronJob).order_by(CronJob.creationDate.desc()), int(page), int(size))
  print(pagination)
  return pagination
