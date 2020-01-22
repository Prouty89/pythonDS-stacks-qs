# Queue

# An ADT that stores items in the order in which they were added.
# Items in a queue are added to the back and removed from the front.

# Customer standing in a line FIFO
# Start first in, come out first out.

# Back       Front
#    0 1 2 3 4
# Left       Back

# insert(0) in O(n) linear time and pop() in O(1) constant time.
# When we insert into [0] the items after it have to SHIFT
# ONE operation

# Basic Queue Operations

# Add to the queue (enqueue)
# Remove from the queue (dequeue)


# Any data type that can be stored in a list can be stored in a queue
# Limited access, because we can only access the data from one place.


# More Queue Operations

# Is the queue empty?
# How many items are in the queue?
# What is next to be removed?

# Real-World Example

# A print queue, so that documents are printed in the order in which they were sent to the machine.

# Recursive by nature

# A queue is either empty or it consists of a front item, and the rest is a queue
from random import random


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Takes in an item and inserts it into the 0th index of the list that is representing the Queue.

        Runtime O(n), or linear, because inserting into the 0th index forces the other items to shift 1 to the right.
        """

        self.items.insert(0, item)

    def dequeue(self):
        """
        Returns and removes the front-most item from the Queue, represented by the last item in the list.

        Runtime O(1), or constant time, because indexing to the end of the list happens in constant time.
        """
        if self.items:

            return self.items.pop()
        return None

    def peek(self):
        """
        Returns the last item in the list which represents the front-most item in the Queue.

        Runtime O(1), or constant time, because indexing to the last item of the list happens in constant time.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the size of the Queue which is represented by the length of the list

        Runtime O(1), or constant time, because we're only returning the length of the list.
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value expressing whether or not the list representing the Queue is empty.

        Runtime O(1), or constant time, because it's only checking for equality
        """
        return self.items == []

    # Challenge

    # Create three classes together, that mock how a print executes a printQueue()

    # PrintQueue Job class should have info about how many pages are left,
    # decrement the page class when we print something.
    # The classes will need to talk to one another.

    class PrintQueue:

        def __init__(self):
            self.items = []

        def enqueue(self, item):
            self.items.insert(0, item)

        def dequeue(self):
            return self.items.pop()

        def is_empty(self):
            return self.items == []


    class Job:

        def __init__(self):
            self.pages = random.randint(1, 11)

        def print_page(self):
            if self.pages > 0:
                self.pages -= 1

        def check_complete(self):
            if self.pages == 0:
                return True
            return False

    class Printer:

        def __init__(self):
            self.current_job = None

        def get_job(self, print_queue):
            try:
                self.current_job = print_queue.dequeue()
            except IndexError:
                return "No more jobs to print."

        def print_job(self, job):
            while job.pages > 0:
                job.print_page()

            if job.check_complete():
                return "Printing complete."
            else:
                return "An error occurred."

