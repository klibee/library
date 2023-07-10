# third-party
# =======================================
import datetime


# function
# =======================================
def timestamp(self):

    current_time = datetime.datetime.now()
    timestamp    = int(current_time.timestamp())

    # bye
    return timestamp