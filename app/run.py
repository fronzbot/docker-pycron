import os
import time
import yaml
from subprocess import call
from crontab import CronTab

DEFAULT_WORK = '/work'
DEFAULT_CONFIG = 'config.yaml'

CONFIG_AT = 'at'
CONFIG_SCHEDULE = 'schedule'
CONFIG_ARGS = 'args'
CONFIG_DAYS = 'days'
CONFIG_HOURS = 'hours'
CONFIG_MINUTES = 'minutes'
CONFIG_SECONDS = 'seconds'


def new_job(cron, filename, config):
    """Create a python job."""
    if CONFIG_ARGS in config:
        print("Found following args: {}".format(config[CONFIG_ARGS]))
        for arg in config[CONFIG_ARGS]:
            filename = "{} {}".format(filename, arg)

    return cron.new(command="python {}".format(filename))


def schedule_job(cron, job, config):
    """Creates scheduling for jobs."""
    try:
        schedule = config[CONFIG_SCHEDULE]
        print("{}: {}".format(CONFIG_SCHEDULE, schedule))
        if CONFIG_DAYS in schedule:
            job.day.every(schedule[CONFIG_DAYS])
        elif CONFIG_HOURS in schedule:
            job.hour.every(schedule[CONFIG_HOURS])
        elif CONFIG_MINUTES in schedule:
            job.minute.every(schedule[CONFIG_MINUTES])
        elif CONFIG_SECONDS in schedule:
            job.second.every(schedule[CONFIG_SECONDS])

    except KeyError:
        print("{} not found in {}".format(CONFIG_SCHEDULE, DEFAULT_CONFIG))

    cron.write()

    return


def create_script_configs(cron, config_file):
    """Create config entries for scripts."""
    yaml_config = load_yaml(config_file)

    for script, config in yaml_config.items():
        filename = "{}/{}.py".format(DEFAULT_WORK, script)
        print("Setting up {}".format(filename))

        job = new_job(cron, filename, config)

        schedule_job(cron, job, config)


def load_yaml(fname):
    """Load yaml file."""
    with open(fname) as cfg_file:
        return yaml.load(cfg_file)

if __name__ == '__main__':
    cron = CronTab(user=True)
    create_script_configs(cron, "{}/{}".format(DEFAULT_WORK, DEFAULT_CONFIG))
