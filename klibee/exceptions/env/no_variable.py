# class
# =======================================
class NoVariableInEnvFileException(Exception):


    # function
    # =======================================
    def __init__(self, var_name):

        message = """
            There is no variable {} at .env file.
        """.format(var_name).replace("  ", "")

        self.var_name  = var_name
        self.message   = message

        super().__init__(self.message)
