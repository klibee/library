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

    # override
    if (host is None):
        host = environment.REDIS_HOST

    if (port is None):
        port = environment.REDIS_PORT

    if (password is None):
        password = environment.REDIS_PASS

    # reader .env
    environment = Environment()

    # go
    client = None

    try:
        # client
        client = redis.Redis(host=host, port=port, password=password)

        # test
        client.set("foo", "bar")
        client.delete("foo")

    except:
        raise Exceptions.CannotConnectRedisException(host)

    # assign
    self.client = client

    # bye
    return client
