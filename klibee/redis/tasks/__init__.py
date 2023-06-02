# this libary
# =======================================
from klibee.redis.connection import connection
from klibee.redis.keys       import Keys
from klibee.environment      import Environment
from klibee.exceptions       import Exceptions

# third-party packages
# =======================================
import uuid
import json


# function
# =======================================
def make_task(self, payload, id_task_type = None):

    # data
    id_task = str(uuid.uuid4())

    task = {
         "id_task": id_task,
    "id_task_type": id_task_type,
         "payload": payload
    }

    # bye
    return task


# function
# =======================================
def enqueue_tasks(self, tasks, queue = None):

    # connection
    redis = connection(self)

    # pipeline
    pipeline = redis.pipeline()

    # override
    if (queue is None):
        environment = Environment()
        queue       = environment.REDIS_QUEUE

    # check
    if (queue is None):
        raise Exceptions.NoVariableInEnvFileException("REDIS_QUEUE")

    # go
    for task in tasks:

        # cast to string
        data     = json.dumps(task)
        cacheKey = Keys().metadata_for_task(task["id_task"])

        # bulk mode
        pipeline.set(cacheKey, data)
        pipeline.expire(cacheKey, 86400) # seconds in a day

        # bulk mode
        pipeline.lpush(queue, task["id_task"])

    # send
    pipeline.execute()


# function
# =======================================
def get_task(self, queue = None):

    # connection
    redis = connection(self)

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
    cacheKey = Keys().metadata_for_task(id_task)
    data     = redis.get(cacheKey)

    # check
    if (data is None):
        raise Exceptions.NoMetadataInRedisException(cacheKey)

    # cast to dict
    data = json.loads(data)

    # bye
    return data


