"""
Stack Data Structure and it's implementation.
"""

from typing import Any

__version__= "1.0.0"

class Stack:
    """
    Stack Data Structure Implementation

    Methods:
    --------
    push(self, x):
        Push the object to the stack.

    pop(self):
        Pop out the last object in the stack.

    isempty(self):
        Return True if stack is empty else False.
    """
    def __init__(self, size:int) -> None:
        """Initialize stack and head pointer. """
        self.stack = list()
        self.head = 0
        self.stack_size = size

    def isempty(self)-> bool:
        """Return whether Stack is empty or not."""
        return self.head == 0

    def push(self, x:Any)-> None:
        """Push object into the stack and increment the head pointer."""
        self.head += 1
        if self.head > self.stack_size:
            print("StackOverFlow: Can't able to insert {x}")
            return None
        self.stack.append(x)
        print(f"Object {x} is pushed in to the stack")

    def pop(self)-> None:
        """Pop the object from the stack"""
        if self.head == 0:
            print("StackUnderFlow!")
            return None
        removed_obj = self.stack.pop()
        self.head -= 1
        print(f"Object {removed_obj} is removed from the stack")

    def traverse(self)-> None:
        """Print the element in the stack."""

        if self.isempty() == True:
            print("There's no object in the stack!")
        else:
            for _ in self.stack:
                print(_, end=" ")
