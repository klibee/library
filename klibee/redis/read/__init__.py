# packages
# ================================================
import json


# function
# ================================================
def get(self, cacheKey):

    # connect
    client = self.connection()

    # get
    data = client.get(cacheKey)

    # check
    if (data is None):
        return None

    # try to cast to dict
    try:
        data = json.loads(data)
    except:
        pass

    # bye
    return data


# function
# ================================================
def has(self, cacheKey):

    # connect
    data = self.get(cacheKey)

    # bye
    return (data is not None)
