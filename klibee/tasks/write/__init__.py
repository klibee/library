# this libary
# =======================================
from klibee.redis         import Redis
from klibee.environment   import Environment
from klibee.exceptions    import Exceptions

# third-party packages
# =======================================
import uuid
import json


# function
# =======================================
def make(self, payload, id_task_type = None):

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
def enqueue(self, data, queue = None, expire = 86400):

    # we can enqueue in bulk mode (a list of objects)
    # or a single object
    tasks = []
    if isinstance(data, list):
        tasks = data
    else:
        tasks.append(data)


    # connection
    redis = Redis().connection()

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
        cacheKey = Redis().keys.metadata_for_task(task["id_task"])

        # bulk mode
        pipeline.set(cacheKey, data)
        pipeline.expire(cacheKey, expire) # seconds in a day

        # bulk mode
        pipeline.lpush(queue, task["id_task"])

    # send
    pipeline.execute()

