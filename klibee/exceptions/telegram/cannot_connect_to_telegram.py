# class
# =======================================
class CannotConnectTelegramException(Exception):


    # function
    # =======================================
    def __init__(self, username, api_id, api_hash):

        message = """
            We were unable to connect to telegram server as user {}.
        """.format(username).replace("  ", "")

        self.username = username
        self.api_id   = api_id
        self.api_hash = api_hash
        self.message  = message

        super().__init__(self.message)
