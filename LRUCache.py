"""
Implementation of an LRU (Least Recently Used) structure for caching
"""

# this hasn't been tested

from typing import TypeVar, Optional, Dict

K = TypeVar('K')
V = TypeVar('V')


class Node:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


def create_node(value: V) -> Node:
    return Node(value)


class LRU:
    def __init__(self, capacity: int = 10):
        self.length: int = 0
        self.head: Node = None
        self.tail: Node = None
        self.capacity: int = capacity

        self.lookup: Dict[K, Node] = {}
        self.reverse_lookup: Dict[Node, K] = {}

    def update(self, key: K, value: V) -> None:
        # check if it exists using the get method
        node = self.lookup.get(key)

        # create new node if it doesn't exist
        if not node:
            node = create_node(value)

            # increase length of linked list
            self.length += 1

            # add to front of linked list
            self.__prepend(node)

            # ensures cache remains no greater than capacity
            self.__trim_cache()

            # update the lookup hashmaps
            self.lookup[key] = node
            self.reverse_lookup[node] = key

        # if it does exist then need to move to front of list
        else:
            self.__detach(node)
            self.__prepend(node)

            # update the node's value
            node.value = value

    def get(self, key: K) -> Optional[V]:

        # check cache to see if value exists
        node = self.lookup.get(key)
        if not node:
            return None

        # update value and move to front
        self.__detach(node)
        self.__prepend(node)

        # return the value found
        return node.value

    def __detach(self, node: Node) -> None:

        # if the node has a previous node
        if node.prev:

            # reassign link to skip the current node
            node.prev.next = node.next

        # do the same as above but in the other direction
        if node.next:
            node.next.prev = node.prev

        # if the node to be removed is the head then reassign head pointer to next in line
        if self.head == node:
            self.head = self.head.next

        # do the same for the tail
        if self.tail == node:
            self.tail = self.tail.prev

        # remove the links from the node
        node.next = None
        node.prev = None

    def __prepend(self, node: Node) -> None:

        # if linked list has no head (and hence no tail) set both to this node
        if not self.head:
            self.head = self.tail = node
            return

        # point to the head
        node.next = self.head

        # point the head to the node
        self.head.prev = node
        self.head = node

    def __trim_cache(self) -> None:

        # continue if the length is within the allotted capacity
        if self.length <= self.capacity:
            return

        # reference the tail
        tail = self.tail

        # remove tail from the linked list
        self.__detach(tail)

        # get the key of the tail
        key = self.reverse_lookup.get(tail)

        # remove the items from the dicts
        del self.lookup[key]
        del self.reverse_lookup[tail]

        # reduce the length
        self.length -= 1
