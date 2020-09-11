import datetime
from crontab import CronTab
from src.commons.utils.crontab import MyCronTab
from cron_descriptor import get_description
import platform


def add_cron_job(cronjob_from_request, cron_job):
    cronjob_raw_expression = cron_job.expression
    cronjob_converted_expression = get_description(cronjob_raw_expression)
    script_command = cron_job.command
    if (cronjob_from_request['log']['logFile'] &
            cronjob_from_request['log']['logFile']):
        command = MyCronTab.cmd_woutput_log_mail(
            script_command,
            str(cron_job.id),
            cronjob_from_request['description']
        )
    elif (cronjob_from_request['log']['sendMail']):
        command = MyCronTab.cmd_woutput_mail(
            script_command,
            cronjob_from_request['description']
        )
    elif (cronjob_from_request['log']['logFile']):
        command = MyCronTab.cmd_woutput_log(script_command, str(cron_job.id))

    status = "On Hold"

    if (platform.system() == 'Windows'):
        cron = CronTab()
        script_path = ''
    else:
        cron = CronTab(user='root')
        script_body = MyCronTab.create_cron_shell_script(cron_job.id, command)
        script_path = MyCronTab.write_cron_shell_file(cron_job.id, script_body)

        job = cron.new(
            command='/bin/bash {0}'.format(script_path),
            comment=str(cron_job.id)
        )
        job.setall(cronjob_raw_expression)
        print("job: ", job)
        print("job.is_valid? ", job.is_valid())
        if job.is_valid():
            status = "Running"
        # cron.write(user='root')
            nextRun = datetime.datetime.now().strftime("%Y-%m-%d")
    return status
