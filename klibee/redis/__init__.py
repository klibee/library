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
    from klibee.redis.read        import get
    from klibee.redis.read        import has
    from klibee.redis.write       import set

    # make
    keys = Keys()

