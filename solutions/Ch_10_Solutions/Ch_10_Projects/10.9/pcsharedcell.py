"""
File: pcsharedcell.py
Project 10.9
Resource for shared data synchonization for the producer-consumer
problem. Guarantees that a writer finishes writing before a reader
and conversely. Only the writer can access the data at startup.
"""

from threading import Condition
from sharedcell import SharedCell

class PCSharedCell(SharedCell):
    """Shared data that sequences reading before writing."""
    
    def __init__(self, data):
        """Can produce but not consume at startup."""
        SharedCell.__init__(self, data)
        self.writeable = True
        self.condition = Condition()

    def beginRead(self):
        """Caller must wait until someone has produced
        the data before accessing it."""
        self.condition.acquire()
        while self.writeable:
            self.condition.wait()
        
    def endRead(self):
        """Let writer know it's ok to write."""
        self.writeable = True
        self.condition.notify()
        self.condition.release()

    def beginWrite(self):
        """Can write only when someone else is not
        writing or reading."""
        self.condition.acquire()
        while not self.writeable:
            self.condition.wait()

    def endWrite(self):
        """Notify reader it's ok to read."""
        self.writeable = False
        self.condition.notify()
        self.condition.release()
