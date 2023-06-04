# this libary
# =======================================
from klibee.redis         import Redis
from klibee.environment   import Environment
from klibee.exceptions    import Exceptions


# third-party packages
# =======================================
import json


# function
# =======================================
def get(self, queue = None):

    # connection
    redis = Redis().connection()

    # override
    if (queue is None):
        environment = Environment()
        queue       = environment.REDIS_QUEUE

    # check
    if (queue is None):
        raise Exceptions.NoVariableInEnvFileException("REDIS_QUEUE")

    # get next
    result = redis.lpop(queue)

    if (result is None):
        return None

    # cast
    id_task = result.decode()

    # cache
    cacheKey = Redis().keys.metadata_for_task(id_task)
    data     = redis.get(cacheKey)

    # check
    if (data is None):
        raise Exceptions.NoMetadataInRedisException(cacheKey)

    # cast to dict
    data = json.loads(data)

    # bye
    return data


# function
# =======================================
def getById(self, id_task, queue = None):

    # connection
    redis = Redis().connection()

    # override
    if (queue is None):
        environment = Environment()
        queue       = environment.REDIS_QUEUE

    # check
    if (queue is None):
        raise Exceptions.NoVariableInEnvFileException("REDIS_QUEUE")

    # cache
    cacheKey = Redis().keys.metadata_for_task(id_task)
    data     = redis.get(cacheKey)

    # check
    if (data is None):
        raise Exceptions.NoMetadataInRedisException(cacheKey)

    # cast to dict
    data = json.loads(data)

    # bye
    return data


# function
# =======================================
def length(self, queue = None):

    # connection
    redis = Redis().connection()

    # override
    if (queue is None):
        environment = Environment()
        queue       = environment.REDIS_QUEUE

    # check
    if (queue is None):
        raise Exceptions.NoVariableInEnvFileException("REDIS_QUEUE")

    # get next
    result = redis.llen(queue)

    # bye
    return result
