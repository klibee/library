# this library
# ================================================
from klibee.environment import Environment
from klibee.logger      import Logger



# class
# ================================================
class Keys:

    # the constructor
    # ================================================
    def __init__(self):
        self.prefix = self.get_prefix()

    # function
    # ================================================
    def get_prefix(self):

        # .env
        environment = Environment()

        # get
        prefix = environment.REDIS_PREFIX

        # check
        if (prefix is None):
            Logger.info("REDIS_PREFIX is not defined in .env")
            prefix = "unset"

        # bye
        return prefix



    # function
    # ================================================
    def metadata_for_task(self, uuid):
        return "{}.tasks.metadata:{}".format(self.prefix, uuid)