
from src.repositories.entity import Entity, Base
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from marshmallow import Schema, fields
from src.commons.utils.crontab import MyCronTab #, get_last_run_from_log

class CronJob (Entity, Base):
  __tablename__ = 'cron_job'
  creationDate =  Column('creation_date',DateTime)
  command = Column(String)
  jobType = Column('job_type',String)
  cronSchedule = Column('cron_schedule',String)
  expression = Column(String)
  lastRun = Column('last_run',DateTime)
  status = Column(String)
  nextRun = Column('next_run',DateTime)

  def __init__(self, creationDate, command, jobType, schedule, expression, lastRun, status, nextRun):
    self.creationDate = creationDate
    self.command = command
    self.jobType = jobType
    self.cronSchedule = schedule
    self.expression = expression
    self.lastRun = lastRun
    self.status = status
    self.nextRun = nextRun

  def job(self):
    cron = MyCronTab.MyCronTab
    job = cron.find_comment(str(id))
    return job
  
  def get_lastrun(self):
    job = self.job()
    last_run, status = MyCronTab.get_last_run_from_log(self)
    return last_run, status

  def update_lastrun(self, session):
    self.lastRun, self.status = self.get_lastrun()
    session.commit()


class CronJobSchema(Schema):
  id = fields.Number()
  creationDate = fields.DateTime("%Y-%m-%d, %H:%M:%S")
  command = fields.Str()
  jobType = fields.Str()
  cronSchedule = fields.Str()
  expression = fields.Str()
  lastRun = fields.DateTime("%Y-%m-%d, %H:%M:%S")
  status = fields.Str()
  nextRun = fields.DateTime("%Y-%m-%d, %H:%M:%S")



