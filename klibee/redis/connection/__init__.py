# library
# ================================================
from klibee.environment import Environment
from klibee.exceptions  import Exceptions


# third-party
# ================================================
import redis


# function
# ================================================
def connection(self, host = None, port = None, password = None):

    # singleton
    if (self.client is not None):
        return self.client

    # reader .env
    environment = Environment()

    # override
    if (host is None):
        host = environment.REDIS_HOST

    if (port is None):
        port = environment.REDIS_PORT

    if (password is None):
        password = environment.REDIS_PASS

    # check
    if (host is None):
        raise Exceptions.NoVariableInEnvFileException("REDIS_HOST")

    if (port is None):
        port = 6379

    # go
    client = None

    try:
        # client
        client = redis.Redis(host=host, port=port, password=password, socket_timeout=3)

        # test
        client.ping()
    except:
        raise Exceptions.CannotConnectRedisException(host)

    # assign
    self.client = client

    # bye
    return client
