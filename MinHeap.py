import math
from typing import List


class MinHeap:

    # not implementing method to update values

    def __init__(self):
        self.data: List[int] = []
        self.length = 0

    def insert(self, value) -> None:

        # set new value the bottom of the heap
        self.data.append(value)

        # bubble the item upwards until MinHeap conditions are met
        self.__heapify_up(self.length)

        # increase the length variable
        self.length += 1

    def delete(self) -> int:

        # if heap is empty
        if self.length == 0:
            return -1

        # remove and store the value at top of tree
        out = self.data[0]

        # reduce the length
        self.length -= 1

        # if only one element in the heap
        if self.length == 0:
            self.data = []
            return out

        # set the very bottom value to the new tree root
        self.data[0] = self.data[self.length]

        # bubble the item downwards until MinHeap conditions are met
        self.__heapify_down(0)

        return out

    def __heapify_down(self, idx: int) -> None:

        # base case -> at the bottom of the tree
        if idx >= self.length:
            return

        # get index of the children
        left_idx = self.__left_child(idx)
        right_idx = self.__right_child(idx)

        # index no longer withing the heap's nodes
        if left_idx >= self.length:
            return

        # parent and child values
        left_val = self.data[left_idx]
        right_val = self.data[right_idx]
        curr_val = self.data[idx]

        # if right is smaller than left, and current is smaller than right then we need to do down the tree to the right
        if (left_val > right_val) and (curr_val > right_val):

            # swap the parent and child
            self.data[idx] = right_val
            self.data[right_idx] = curr_val

            # recurse
            self.__heapify_down(right_idx)

        # if left is smaller than right, and current is smaller than left then we need to do down the tree to the left
        if (right_val > left_val) and (curr_val > left_val):

            # swap the parent and child
            self.data[idx] = left_val
            self.data[left_idx] = curr_val

            # recurse
            self.__heapify_down(left_idx)

        # could also handle condition where there's only a left child and no right child

    def __heapify_up(self, idx: int) -> None:

        # base case -> at the top (root) of the tree
        if idx == 0:
            return

        # get index of parent node
        par = self.__parent(idx)

        # get the parent node's value
        parent_val = self.data[par]

        # current value
        val = self.data[idx]

        # if parent is larger, the current node needs to go upwards in the MinHeap
        if parent_val > val:

            # swap positions of parent and child
            self.data[idx] = parent_val
            self.data[par] = val

            # recurse
            self.__heapify_up(par)

    def __parent(self, idx: int) -> int:
        return math.floor((idx - 1) / 2)

    def __left_child(self, idx: int) -> int:
        return (2 * idx) + 1

    def __right_child(self, idx: int) -> int:
        return (2 * idx) + 2


def test_min_heap():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    heap.insert(2)
    heap.insert(7)
    heap.insert(6)
    heap.insert(4)

    assert heap.delete() == 1
    assert heap.delete() == 2
    assert heap.delete() == 3
    assert heap.delete() == 4
    assert heap.delete() == 5
    assert heap.delete() == 6
    assert heap.delete() == 7
    assert heap.delete() == 8
    assert heap.delete() == -1

test_min_heap()


