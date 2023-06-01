# class
# =======================================
class FileDoestNotExistsException(Exception):


    # function
    # =======================================
    def __init__(self, filepath_origin):

        message = """
            There is no file at {}.
        """.format(filepath_origin).replace("  ", "")

        self.filepath_origin  = filepath_origin
        self.message          = message

        super().__init__(self.message)
