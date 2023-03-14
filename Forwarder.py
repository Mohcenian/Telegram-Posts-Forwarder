import sys
import time

import socks
from pyrogram import (
    Client, filters, idle,
)
from pyrogram.types import (
    Message
)


def generate_string_(lenght: int = None) -> str:  # ---password
    letters = string.ascii_letters + string.digits
    return (''.join(random.choice(letters) for _ in range(lenght)))


from config import *

# -----------------------------------------------------------
print("START")
client_session = "1AZWarzkBu0VWFz0oMUcXCMaK51VAuJCcvOjmuBHB-jYsTPeHHf1aPZhGJ5o1YN4HU1sPacD_WYH-grBUEErVNOq5XaB0xaJt4yXE2ZWnxMewnTVlRmzDkpAePEP-9K3V33diki148PlS4t_FLkPovbQGbH4wGva71n2FaNl1rjFH_Ntd30t3dK36PvSVFYjJUIdgcIhqKIKY__grUIAK7PhNBFBTrsFFRqYlL1HnG-mbcoDU-Gi_avRwrBja8MkOGIDXpc9kgSdCrb0-DH2dCSH_7xlmuG62MAAgLghTpZpdW1wfGZ_jCAYMU8sPXKxV1n9gvFWutMm9kBqZKhe1MoxfeBGQaMs=
"

# ------------------------------------------------check proxy


# -----------------------
# **********************************************************************************************************************
temp.start()

from_channel_list = ["", "", ""] #Target Channels Username Without @
to_channel_list = [] # Your Destination Channel's UserID


@temp.on_message(filters.channel & filters.incoming)
def channel_msg_check(api: Client, msg: Message):
            for channel_ in to_channel_list:
                temp.send_message(channel_, text_to_send)


# -----------------------
idle()
try:
    temp.disconnect()
except:
    pass
try:
    temp.stop()
except:
    pass
try:
    temp.terminate()
except:
    pass

print("END")
