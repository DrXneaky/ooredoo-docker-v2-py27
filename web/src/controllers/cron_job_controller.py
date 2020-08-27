
from src.entities.cron_job import CronJob, CronJobSchema
from src.repositories.cronjob_repository import get_cron_jobs

def get_cron_jobs_schema(session, page, size):
  schema = CronJobSchema(many=True)
  page = get_cron_jobs(session, page, size)
  for cronjob in page.items:
    cronjob.update_lastrun(session)
  page.items = schema.dump(page.items)
  return page.__dict__
  