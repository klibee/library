# other classes
# =======================================
from klibee.redis.keys import Keys


# class
# =======================================
class Redis:

    # the constructor
    from klibee.redis.constructor import __init__

    # load
    from klibee.redis.connection  import connection
    from klibee.redis.channel     import channel

    # make
    keys = Keys()

