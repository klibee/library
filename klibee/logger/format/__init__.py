# this library
# ================================================
from klibee.logger.constants import Constants


# modules
# ================================================
import datetime


# function
# ================================================
def format_message(args, logcolor = None, logtype = None, entryLine = False):

    # remove the first items in args because it is the logger address 
    # (ex. <lib.helpers.logger.Logger object at 0x7f5bc383af40>)
    args = list(args)

    if (not isinstance(args[0], str)):
        args.pop(0)

    # the message
    message = " ".join(str(x) for x in args)
    message = message.strip()

    # the date
    date = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

    # log items
    items = []
    items.append("[")
    items.append(Constants.COLOR_BLUE)
    items.append(date)
    items.append(Constants.ENDC)
    items.append("]")
    items.append(" ")
    items.append("[")
    items.append(logcolor)
    items.append(logtype)
    items.append(Constants.ENDC)
    items.append("]")
    if (logtype == Constants.INFO):
        items.append("   ")
    elif (logtype == Constants.ERROR):
        items.append("  ")

    items.append(" ")

    if (entryLine):
        items.append(logcolor)

    items.append(message)

    if (entryLine):
        items.append(Constants.ENDC)

    # the log string
    return ''.join(items)
