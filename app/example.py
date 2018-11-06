"""Example script showing use of internal pycron helpers."""

from pycron import LOGGER

LOGGER.info("Howdy! This is an example script output.")

def run():
    LOGGER.info("And this is what happens if I'm called in a function.")

if __name__ == "__main__":
    run()
