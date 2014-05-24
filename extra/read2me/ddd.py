__author__ = 'jonathan'

import threading
import logging
import time
logging.basicConfig(level=logging.INFO,
                    format="[%(threadName)-10s] %(message)s")

def block(event):
    logging.info("Blocks until event is set")
    event_set=event.wait() # returns True when event is set
    logging.info("Is set: %s", event_set)
    return

def nonblock(event):
    while True:
        logging.info("Waits until event is set or timeout reached")
        # returns True when event is set, false when timeout reached
        event_set=event.wait(0.5)
        if event_set: # event set
            break
        logging.info("Time out reached: Doing other useful work")
    # isSet() return true if event is set, else returns false
    logging.info("Is set: %s", event.isSet())

def main():
    event=threading.Event()
    t1=threading.Thread(target=block,
                        name="block",
                        args=(event,))
    t2=threading.Thread(target=nonblock,
                        name="nonblock",
                        args=(event,))
    t1.start()
    t2.start()
    time.sleep(3)
    logging.info("Setting Event")
    event.set()
if __name__=="__main__":
    main()