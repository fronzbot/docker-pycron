"""
To enable logging to syslog in your custom scripts,
add the following to the top of your python script:

    from pycron import LOGGER

To use logging, you replace any "print" statements with
LOGGER.<LEVEL> where <LEVEL> can be:
    - debug
    - info
    - warning
    - error

So to log an error message, you would state:

    LOGGER.error("Some error message")

"""

import logging
import logging.handlers

LOGGER = logging.getLogger('pycron')
LOGGER.setLevel(logging.DEBUG)

HANDLER = logging.handlers.SysLogHandler('/dev/log')
FORMATTER = logging.Formatter('%(levelname)s [%(module)s.%(funcName)s]: %(message)s')
HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(HANDLER)
