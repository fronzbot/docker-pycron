# docker-python

This is a generic python docker used to run custom scripts and what not.

## Usage

Map the `/work` directory to wherever you want your scripts stored and the `/share` directory to wherever you want saved data to go (not needed, but can be useful).

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
