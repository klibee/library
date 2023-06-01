# class
# =======================================
class CannotCastMetadataException(Exception):


    # function
    # =======================================
    def __init__(self, key):

        message = """
            We were unable to cast {} to dictionary.
        """.format(key).replace("  ", "")

        self.key     = key
        self.message = message

        super().__init__(self.message)
