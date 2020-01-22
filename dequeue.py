# Dequeue = Double ended queue

# An ADT that resembles both a stack and a queue
# Items in a dequeue can be added to and removed from both the front and the back.

# Use a list

# Front         Rear
#      0 1 2 3 4
# Left          Right

# insert(0) in O(n) time      append() in O(1) time
# insert(0) in O(n) time         pop() in O(1) time

# Deque Operations

# Add to the dequeue (front and rear)
# Remove from the dequeue (front and rear)

# Is the dequeue empty?
# How many items are in the deque?
# What is next to be removed from either end?

# Queue = FIFO
# Stack = LIFO
# Deque = BOTH, up to the programmer

# Any data type that can be stored in a list can be stored in a deque
# Limited access, because we can only access the data from either end

# Interview example - Check whether or not a string is a palindrome

class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """

        Takes an item as a parameter and inserts it into the [0] that represents the Deque.

        Runtime is linear, or O(n) because when an item is inserted all other items need to shift one to the right.

        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """

        Takes an item as a parameter and appends the item to the list that represents the Deque.

        Runtime is constant because the item is added to the end of the list.

        """
        self.items.append(item)

    def remove_front(self):
        """

        Removes item from the front of the list representing the front of the Deque.

        Runtime is linear, or O(n) because when an item is removed from the fright
        all other items need to shift one to the left.

        """
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """

        Removes an item from the end of the list which represents the end of the Deque.

        Runtime is constant, because the item is simply removed from the end.

        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """

        Inspects, returns the value found at the 0th index of the list, representing the front of the Deque.

        Runtime is constant, or O(1) because we're just looking at an item.

        """
        if self.items:
            return self.items(0)
        return None

    def peek_rear(self):
        """

        Inspects the last item (-1) in the list, representing the rear of the Deque

        Runtime is constant, or 0(1) because we're just looking at an item.

        """
        if self.items:
            return self.items(-1)
        return None

    def size(self):
        """

        Returns the number of items in the list, representing the Deque

        Runtime is constant, O(1) because no operations are being run on the Deque

        """
        return len(self.items)

    def is_empty(self):
        """

        Checks the length against an empty list, returning True or False

        Runtime is constant, O(1) because no operations are being run on the Deque

        """
        return self.items == []


# Challenge Deque

# Use a Deque that takes in an input string, returning true if a string is a palindrome, false if not.
# Mom, level, kayak


# Loop through the input string and add all the characters to the rear of the deque.

# Adding an item to the rear of the deque is a constant time operation.

# As long as the deque's size is >=2 , remove the front-most item and the rear-most item from the deque and store each
# in its on variable.

# If the size of the deque eventually becomes <2 (meaning 1 or 0), the string was a palindrome, return True.

class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def check_palindrome(input_str):
    my_d = Deque()
    for char in input_str:
        my_d.add_rear(char)

    while my_d.size() >= 2:
        front_item = my.d.remove_front()
        rear_item = my_d.remove_rear()

        if front_item != rear_item:
            return False

    return True


print(check_palindrome('racecar'))
print(check_palindrome('oranges'))

# Problem solving with algorithms and data structures using python.
