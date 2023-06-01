# class
# =======================================
class CannotConnectRedisException(Exception):


    # function
    # =======================================
    def __init__(self, host):

        message = """
            We were unable to connect to redis server at {}.
        """.format(host).replace("  ", "")

        self.host     = host
        self.message  = message

        super().__init__(self.message)
