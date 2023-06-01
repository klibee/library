# this library
# ================================================
from klibee.logger.constants import Constants
from klibee.logger.format    import format_message


# modules
# ================================================
import logging


# function
# ================================================
def error(*args):
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.error(format_message(args, Constants.COLOR_DANGER, Constants.ERROR, entryLine=True))