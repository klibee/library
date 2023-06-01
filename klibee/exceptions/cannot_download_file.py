# class
# =======================================
class CannotDownloadFileException(Exception):


    # function
    # =======================================
    def __init__(self, filepath_origin, filepath_destiny):

        message = """
            We cannot download this file {}
            to this destination {}.
        """.format(filepath_origin, filepath_destiny).replace("  ", "")

        self.filepath_origin  = filepath_origin
        self.filepath_destiny = filepath_destiny
        self.message          = message

        super().__init__(self.message)
