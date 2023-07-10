# library
# ================================================
from klibee.exceptions  import Exceptions


# third-party packages
# ================================================
from telethon.tl.types import Channel


# function
# ================================================
def get_conversations(self):

    # client
    client = self.connection()

    # items
    conversations = client.iter_dialogs(limit=None)

    # result
    result = []

    # read
    for conversation in conversations:

        # check
        if not isinstance(conversation.entity, Channel):
            continue

        # add
        result.append({
                 "id": abs(conversation.id),
        "description": conversation.name
        })

    # bye
    return result

