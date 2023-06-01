# library
# =======================================
from klibee.environment import Environment
from klibee.redis       import Redis
from klibee.exceptions  import Exceptions
from klibee.logger      import Logger


# class
# =======================================
class Klibee:


    Environment = Environment()
    Redis       = Redis()
    Exceptions  = Exceptions()
    Logger      = Logger()

