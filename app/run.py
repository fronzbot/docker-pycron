import os
import time
from ruamel.yaml import YAML
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


def new_job(cron, filename, config):
    """Create a python job."""
    if CONFIG_ARGS in config:
        print("Found following args: {}".format(config[CONFIG_ARGS]))
        for arg in config[CONFIG_ARGS]:
            filename = "{} {}".format(filename, arg)

    return cron.new(command="/usr/local/bin/python {}".format(filename))


def schedule_job(cron, job, config):
    """Creates scheduling for jobs."""
    try:
        schedule = config[CONFIG_SCHEDULE]
        print("{}: {}".format(CONFIG_SCHEDULE, schedule))
        if CONFIG_DAYS in schedule:
            job.every(schedule[CONFIG_DAYS]).days()
        elif CONFIG_HOURS in schedule:
            job.every(schedule[CONFIG_HOURS]).hours()
        elif CONFIG_MINUTES in schedule:
            job.every(schedule[CONFIG_MINUTES]).minutes()
        else:
            print("Invalid entry {}".format(schedule))

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
    yaml = YAML(typ='safe')
    with open(fname) as cfg_file:
        return yaml.load(cfg_file)

if __name__ == '__main__':
    cron = CronTab(user='root')
    create_script_configs(cron, "{}/{}".format(DEFAULT_WORK, DEFAULT_CONFIG))
    cron.write('/etc/cron.d/pycron')
