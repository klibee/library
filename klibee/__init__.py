# library
# =======================================
from klibee.environment import Environment
from klibee.exceptions  import Exceptions
from klibee.logger      import Logger
from klibee.redis       import Redis


# class
# =======================================
class klibee:


    environment = Environment()
    exceptions  = Exceptions()
    logger      = Logger()
    redis       = Redis()

