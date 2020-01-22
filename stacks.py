# What makes the stack Unique?
# Stack stores items in the order in which they were added
# Items are added to and removed from the "top" of a stack
# PANCAKES (LIFO)
# What built-in Python data type is mutable and stores an ordered collection of items?
# A LIST

# Basic Stack Operations
# Add to the stack
# Remove from the stack
#     Bottom       Top
#          0 1 2 3 4
#      Left        Right

# Runtime considerations: append() and pop() in 0(1) time

# More stack operations:
# Is the stack empty?
# How many items are in the stack?
# What is next to be removed?


# Stack Data
# Any data type that can be stored in a list can be stored in a stack
# Limited access because we can only access the data from one place

# Real-world examples:
# A linter in a text editor can detect missing symbols
# Revering the characters in a string
# Stacks are recursive data structures: it is either empty or it consists of a top item and the rest, the stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the list,
        returns nothing

        The runtime for this method is O(1), or constant time, because appending to the end of a list happens in
        constant time. Index to the last item.
        """

        self.items.append(item)

    def pop(self):
        """
        Removes and returns the last item for the list, which is also the top item of the Stack

        The runtime for this method is O(1), or constant time, because appending to the end of a list happens in
        constant time. Index to the last item and return it.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
        Returns the last item in the list, which is the item at the top of the Stack

        This method runs in constant time because indexing into a list happens in constant time.
        """

        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the length of the list representing the Stack

        This method runs in constant time because finding the length of the list happens in constant time
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns boolean value describing whether or not the Stack is empty

        Testing for equality happens in constant time.
        """
        return self.items == []

# Challenge Requirements

# String should only contain opening and closing symbols

# Fail Fast


