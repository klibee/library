# packages
# ================================================
import json


# function
# ================================================
def set(self, cacheKey, data):

    # connect
    client = self.connection()

    # cast
    if (isinstance(data, dict) or isinstance(data, list)):
        data = json.dumps(data)
    elif (isinstance(data, bool)):
        data = int(data)

    # bye
    return client.set(cacheKey, data)
