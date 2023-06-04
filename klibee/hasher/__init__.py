# diwo
# =======================================
from klibee.logger import Logger


# third-party libraries
# ================================================
import json
import hashlib


# class
# ================================================
class Hasher:

    # function
    # ================================================
    def md5(self, obj):

        # cast
        myStr = obj
        if (isinstance(obj, dict)):
            myStr = json.dumps(obj)

        # go
        try:
            return hashlib.md5(myStr.encode('utf-8')).hexdigest()
        except:
            Logger.error("Cannot hash text")
            Logger.error(myStr)

        return None

