# this libary
# =======================================
from klibee.redis.connection import connection


# third-party packages
# =======================================
import uuid
import json


# function
# =======================================
def make_task(self, payload):

    # data
    id_task = str(uuid.uuid4())

    task = {
        "id_task": id_task,
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

    # queue name
    queue = Helpers.Environment.REDIS_QUEUE

    # go
    for task in tasks:

        # cast to string
        data     = json.dumps(task)
        cacheKey = Helpers.Redis.Keys.metadata_for_task(task["id_task"])

        # bulk mode
        pipeline.set(cacheKey, data)
        pipeline.expire(cacheKey, 86400) # seconds in a day

        # bulk mode
        pipeline.lpush(queue, task["id_task"])

    # send
    pipeline.execute()

