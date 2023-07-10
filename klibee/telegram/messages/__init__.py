# library
# ================================================
from klibee.exceptions  import Exceptions


# third-party packages
# ================================================
from telethon.tl.functions.messages import GetHistoryRequest


# function
# ================================================
def get_messages(self, id_channel):

    # client
    client = self.connection()

    # read
    messages = client.iter_messages(entity=id_channel, limit=1000)

    # result
    result = []

    # go
    for message in messages:

        # data
        data = message.to_dict()

        # date
        date = int(data["date"].timestamp())

        # go
        msg = {
             "id": data["id"],
           "date": date,
        "message": data["message"],
        }
        
        result.append(msg)

    # bye
    return result

