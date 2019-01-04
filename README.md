# docker-pycron

![Docker Pulls](https://img.shields.io/docker/pulls/fronzbot/pycron.svg)
![Github tag](https://img.shields.io/github/tag-date/fronzbot/docker-pycron.svg)

This is a generic python docker used to run custom scripts and what not.  [Docker Hub URL](https://hub.docker.com/r/fronzbot/pycron)

## Usage

Please note that this docker uses Python 3.7 and has the following packages installed:

```
cron
ffmpeg
imagemagick
gifsicle
logrotate
```

Additional packages can be installed in the docker using `apt-get install`, or you can request they be added to the docker image.

### Volume Maps

Map the `/work` directory to wherever you want your scripts stored and the `/share` directory to wherever you want saved data to go (not needed, but can be useful).

### First time setup

The first time you install the container, a `config.yaml` and `example.py` file will be placed in your mapped `work` volume.  These just show the syntax for using the container.  Once you're ready to set everything up, you can delete or modify those files.  The next time the container is installed or restarted, it will look for the existance of `config.yaml` and will only create a new example version if one does not already exist.

### Scheduling Scripts

In your `/work` directory, create a file called `config.yaml`.  This config file will define all of your scripts and when they should be scheduled.  Currently `minutes`, `hours`, and `days` are supported.

For exampe, if you have a script in your `/work` directory called `my_script.py`, and you wanted this to run every two hours, your `config.yaml` would look like the following:

```yaml
my_script:
  schedule:
    hours: 2
```

If you had a second script called `fast_script.py` that you wanted to schedule to run eevry five minutes, you would modify your `config.yaml` to look like the following:

```yaml
my_script:
  schedule:
    hours: 2

fast_script:
  schedule:
    minutes: 5
```

Note that any time you edit your `config.yaml` file you will need to restart the container.  Script edits can be done on-the-fly without restarts.

### Logging scripts

You can add print messages to your scripts which are then printed to `/var/log/syslog` (useful for running on [unraid](https://unraid.net) so you can view your script outputs in the log window).  To do this, simply add the following to the top of your script(s):

```python
from pycron import LOGGER
```

You can then create log statements by using the `LOGGER.[LEVEL]` syntax where `[LEVEL]` can be `debug`, `info`, `warning`, or `error`.  So to write an error message to the log, you would use the following syntax (instead of using `print()`):

```python
LOGGER.error("Oh no, something went wrong!")
```

### Custom Python Packages

If you want to install custom python packages without needing to perform a `pip install` on every docker restart, you can add a file called `my_requirements.txt` to your `/work` directory.  You may add packages here with a version number.  For example, If you want to install a specific version of the `sqlalchemy` but just want a minimum version of `requests`, your `my_requirements.txt` file would look like the following:

```
sqlalchemy==1.2.12
requests>=2.0.0
```

Each line represents a package and you can add as many as you'd like!

By default, the following python packages are installed:

```
python-crontab
ruamel.yaml
```
