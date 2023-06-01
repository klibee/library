# library
# =======================================
from klibee.environment import Environment
from klibee.exceptions  import Exceptions
from klibee.files       import Files
from klibee.logger      import Logger
from klibee.random      import Random
from klibee.redis       import Redis


# class
# =======================================
class klibee:


    environment = Environment()
    exceptions  = Exceptions()
    files       = Files()
    logger      = Logger()
    redis       = Redis()
    random      = Random()

