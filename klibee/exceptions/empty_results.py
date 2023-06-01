# class
# =======================================
class EmptyResultsException(Exception):


    # function
    # =======================================
    def __init__(self, oid):

        message = """
            There is not results for: {}.
        """.format(oid).replace("  ", "")

        self.oid     = oid
        self.message = message

        super().__init__(self.message)
