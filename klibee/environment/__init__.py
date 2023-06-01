# third-party
# ================================================
from dotenv import dotenv_values


# class
# =======================================
class Environment:

    # function
    # ================================================
    def __init__(self):

        # load .env file in root project directory
        items = dotenv_values(".env")

        # assign each var to this class
        for key, val in items.items():

            # cast
            if (val == 'true') or (val == 'True'):
                val = True

            if (val == 'false') or (val == 'False'):
                val = False

            # set
            setattr(self, key, val)



    # function
    # ================================================
    def __getattr__(self, attr):
        return None


