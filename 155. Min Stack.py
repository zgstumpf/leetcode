from typing import Union


class Node:
    """
    A node in a MinStack.
    """

    # Should be Union[Node, None], but this throws error because
    # Node isn't defined yet. Outside of LeetCode, this can be fixed
    # with: from __future__ import annotations
    def __init__(self, val: int, below: Union['Node', None]):
        """
        Initialize the Node object.

        - val (int): Value of the node
        - below (Node): Points to a different node. Each node in a MinStack points
        to the node below itself, except for the first node pushed, which points
        to None.
        """
        self.val = val
        self.below = below


class MinStack:
    """
    A stack data structure enabling O(1) retrieval of the minimum element.
    """

    # A MinStack consists of 2 pointers (_top and _min) to different
    # Node objects.
    # Think of _top and _min as separate stacks.
    # _top is the main stack.
    # _min is a parallel stack that stores the minimum value in _top.

    # Example:
    #  _top        _min
    #  -----------------
    #  6            1
    #  1            1
    #  4            2
    #  2            2
    #  None         None

    def __init__(self):
        """
        Initialize the MinStack object.
        """
        self._top = None
        self._min = None

    def push(self, val: int) -> None:
        """
        Puts an element on the top of stack.

        - val (int): Value of the element

        """
        self._top = Node(val, self._top)

        if self._min is None:
            self._min = Node(val, self._min)
            return

        if val < self._min.val:
            self._min = Node(val, self._min)
        else:
            # Get top node of _min, add it to top of _min - again.
            # It is still the minimum value.
            self._min = Node(self._min.val, self._min)

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        if self._top is None:
            return

        self._top = self._top.below

        # If you pop an element from the _top stack, you must also
        # pop an element from the parallel _min stack.
        # Looking at the example stack, if 6 and 1 were popped and the _min
        # stack was unchanged, the minimum would be 1, which is wrong.
        self._min = self._min.below

    def top(self) -> int:
        """
        Returns the value of the the top element of the stack, or None if the
        stack is empty.

        """
        return self._top.val if self._top else None

    def getMin(self) -> int:
        """
        Returns the value of the minimum element in the stack, or None if the
        stack is empty.
        """
        return self._min.val if self._min else None
