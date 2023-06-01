# library
# ================================================
from klibee.environment import Environment


# function
# ================================================
def channel(self, channel = None):

    # override
    if (channel is None):
        channel = environment.REDIS_CHANNEL

    # reader .env
    environment = Environment()

    # connect
    client = self.connection()

    # listener for the channel
    pubsub = client.pubsub()
    pubsub.subscribe(environment.REDIS_CHANNEL)

    # bye
    return pubsub
