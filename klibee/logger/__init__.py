# modules
# ================================================
import datetime
import logging

# class
# ================================================
class Logger:

    COLOR_DANGER  = '\033[91m' # red
    COLOR_SUCCESS = '\033[92m' # green
    COLOR_INFO    = '\033[93m' # yellow
    COLOR_BLUE    = '\033[94m' # blue
    INFO          = 'INFO'
    SUCCESS       = 'SUCCESS'
    ERROR         = 'ERROR'
    ENDC          = '\033[0m'


    # function
    # ================================================
    def format(args, logcolor = None, logtype = None, entryLine = False):

        # remove the first items in args because it is the logger address 
        # (ex. <lib.helpers.logger.Logger object at 0x7f5bc383af40>)
        args = list(args)
        args.pop(0)

        # the message
        message = " ".join(str(x) for x in args)
        message = message.strip()

        # the date
        date = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

        # log items
        items = []
        items.append("[")
        items.append(Logger.COLOR_BLUE)
        items.append(date)
        items.append(Logger.ENDC)
        items.append("]")
        items.append(" ")
        items.append("[")
        items.append(logcolor)
        items.append(logtype)
        items.append(Logger.ENDC)
        items.append("]")
        if (logtype == Logger.INFO):
            items.append("   ")
        elif (logtype == Logger.ERROR):
            items.append("  ")

        items.append(" ")
        
        if (entryLine):
            items.append(logcolor)

        items.append(message)

        if (entryLine):
            items.append(Logger.ENDC)

        # the log string
        return ''.join(items)



    # function
    # ================================================
    def info(*args):
        logging.basicConfig(format='%(message)s', level=logging.INFO)
        logging.info(Logger.format(args, Logger.COLOR_INFO, Logger.INFO))


    # function
    # ================================================
    def success(*args):
        logging.basicConfig(format='%(message)s', level=logging.INFO)
        logging.info(Logger.format(args, Logger.COLOR_SUCCESS, Logger.SUCCESS, entryLine=True))


    # function
    # ================================================
    def error(*args):
        logging.basicConfig(format='%(message)s', level=logging.INFO)
        logging.error(Logger.format(args, Logger.COLOR_DANGER, Logger.ERROR, entryLine=True))

