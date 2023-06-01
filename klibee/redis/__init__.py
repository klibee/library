# class
# =======================================
class Redis:

    # the constructor
    def __init__(self):
        self.client = None

    # load
    from klibee.redis.connection import connection
    from klibee.redis.channel    import channel
