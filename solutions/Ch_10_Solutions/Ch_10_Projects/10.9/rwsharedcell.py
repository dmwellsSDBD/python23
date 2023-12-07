"""
File: rwsharedcell.py
Project 10.9
Resource for shared data synchonization for the general readers and writers
problem. Guarantees that a writer finishes writing before readers can
read and other writers can write. Also supports concurrent reading.
"""

from threading import Condition
from sharedcell import SharedCell

class RWSharedCell(SharedCell):
    """Synchronizes readers and writers around shared data,
    to support concurrent reading and safe writing."""
    
    def __init__(self, data):
        """Sets up the conditions and count of active readers."""
        SharedCell.__init__(self, data)
        self.writing = False
        self.readerCount = 0
        self.okToRead = Condition()
        self.okToWrite = Condition()

    def beginRead(self):
        """Waits until a writer is not writing or the writers
        condition queue is empty. Then increments the reader
        count and notifies the next waiting reader."""
        self.okToRead.acquire()
        self.okToWrite.acquire()
        while self.writing or len(self.okToWrite._waiters) > 0:
            self.okToRead.wait()
        self.readerCount += 1
        self.okToRead.notify()
        
    def endRead(self):
        """Notifies a waiting writer if there are
        no active readers."""
        self.readerCount -= 1
        if self.readerCount == 0:
            self.okToWrite.notify()
        self.okToWrite.release()
        self.okToRead.release()

    def beginWrite(self):
        """Can write only when someone else is not
        writing and there are no readers are ready."""
        self.okToWrite.acquire()
        self.okToRead.acquire()
        while self.writing or self.readerCount != 0:
            self.okToWrite.wait()
        self.writing = True

    def endWrite(self):
        """Notify the next waiting writer if the readers
        condition queue is empty. Otherwise, notify the
        next waiting reader."""
        self.writing = False
        if len(self.okToRead._waiters) > 0:
            self.okToRead.notify()
        else:
            self.okToWrite.notify()
        self.okToRead.release()
        self.okToWrite.release()
