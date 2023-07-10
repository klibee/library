# library
# =======================================
from klibee.dates       import Dates
from klibee.environment import Environment
from klibee.exceptions  import Exceptions
from klibee.files       import Files
from klibee.hasher      import Hasher
from klibee.logger      import Logger
from klibee.random      import Random
from klibee.redis       import Redis
from klibee.tasks       import Tasks


# class
# =======================================
class klibee:

    dates       = Dates()
    environment = Environment()
    exceptions  = Exceptions()
    files       = Files()
    hasher      = Hasher()
    logger      = Logger()
    redis       = Redis()
    tasks       = Tasks()

