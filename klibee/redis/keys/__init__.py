# this library
# ================================================
from klibee.environment import Environment
from klibee.exceptions  import Exceptions



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
            raise Exceptions.NoVariableInEnvFileException("REDIS_PREFIX")

        # bye
        return prefix



    # function
    # ================================================
    def metadata_for_task(self, uuid):
        return "{}.myproject.tasks.metadata:{}".format(self.prefix, uuid)