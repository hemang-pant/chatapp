from old_msg_server.client import Client
import time
from threading import Thread

c1 = Client("tim")
c2 = Client("name")


def update_messages():
    """
    updates the local list of messages
    :return: None
    """
    msgs = []
    run = True
    while run:
        time.sleep(0.1)  
        new_messages = c1.get_messages()  
        msgs.extend(new_messages)  

        for msg in new_messages:  
            print(msg)

            if msg == "{quit}":
                run = False
                break


Thread(target=update_messages).start()

c1.send_message("hello")
time.sleep(5)
c2.send_message("hello")
time.sleep(5)
c1.send_message("whats up")
time.sleep(5)
c2.send_message("Nothing much")
time.sleep(5)

c1.disconnect()
time.sleep(2)
c2.disconnect()