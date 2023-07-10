# library
# ================================================
from klibee.environment import Environment
from klibee.exceptions  import Exceptions


# third-party packages
# ================================================
from telethon import TelegramClient


# function
# ================================================
def connection(self, api_id = None, api_hash = None, username = None):

    # singleton
    if (self.client is not None):
        return self.client

    # reader .env
    environment = Environment()

    # override
    if (api_id is None):
        api_id = environment.TELEGRAM_API_ID

    if (api_hash is None):
        api_hash = environment.TELEGRAM_API_HASH

    if (username is None):
        username = environment.TELEGRAM_USERNAME

    # check
    if (api_id is None):
        raise Exceptions.NoVariableInEnvFileException("TELEGRAM_API_ID")
    elif (api_id is None):
        raise Exceptions.NoVariableInEnvFileException("TELEGRAM_API_HASH")
    elif (username is None):
        raise Exceptions.NoVariableInEnvFileException("TELEGRAM_USERNAME")

    # go
    client = None

    try:
        # client
        client = TelegramClient(username, api_id, api_hash)
        client.start()
    except:
        raise Exceptions.CannotConnectTelegramException(username, api_id, api_hash)

    # assign
    self.client = client

    # bye
    return self.client
