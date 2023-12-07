"""
File: sharedcell.py
Abstract resource for shared data synchonization for readers and writers
problems. Includes the read and write methods and the shared data.
Subclasses add conditions, counts, and flags, as well as
beginRead, endRead, beginWrite, and endWrite.
"""

from threading import Condition

class SharedCell(object):
    """Synchronizes readers and writers around shared data,
    with specific protocols determined by subclasses."""
    
    def __init__(self, data):
        """Sets up the data."""
        self.data = data
        
    def read(self, readerFunction):
        """Observe the data in the shared cell."""
        self.beginRead()
        # Enter reader's critical section
        result = readerFunction(self.data)
        # Exit reader's critical section
        self.endRead()
        return result

    def write(self, writerFunction):
        """Modify the data in the shared cell."""
        self.beginWrite()
        # Enter writer's critical section
        result = writerFunction(self.data)
        # Exit writer's critical section
        self.endWrite()
        return result

