# class
# =======================================
class NoMetadataInRedisException(Exception):


    # function
    # =======================================
    def __init__(self, cache_key):

        message = """
            We were unable to get {} from redis server.
        """.format(cache_key).replace("  ", "")

        self.cache_key = cache_key
        self.message   = message

        super().__init__(self.message)
