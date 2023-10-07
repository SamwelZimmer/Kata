class BinaryNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def breadthFirstSearch(head: BinaryNode, needle: int) -> bool:

    # would ideally be a true queue data structure rather than pythons built-in ArrayList
    queue = [head]

    while len(queue) > 0:

        # dequeue the item from front of queue
        curr: BinaryNode = queue.pop(0)

        # search -> leave the loop if we find the desired item
        if curr.value == needle:
            return True

        # enqueue the left and right children if they exist
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return False  # If the loop finishes without finding the needle


def test_breadthFirstSearch():
    # Build a sample binary tree:
    #       5
    #     /   \
    #    3     8
    #   / \   / \
    #  1   4 6   9

    leaf1 = BinaryNode(1)
    leaf2 = BinaryNode(4)
    leaf3 = BinaryNode(6)
    leaf4 = BinaryNode(9)

    node1 = BinaryNode(3, leaf1, leaf2)
    node2 = BinaryNode(8, leaf3, leaf4)

    root = BinaryNode(5, node1, node2)

    assert breadthFirstSearch(root, 5) == True  # root value
    assert breadthFirstSearch(root, 3) == True  # left child of root
    assert breadthFirstSearch(root, 8) == True  # right child of root
    assert breadthFirstSearch(root, 1) == True  # left leaf
    assert breadthFirstSearch(root, 9) == True  # right leaf
    assert breadthFirstSearch(root, 7) == False  # non-existent value
    assert breadthFirstSearch(root, 0) == False  # non-existent value
    assert breadthFirstSearch(root, 10) == False  # non-existent value

    print("All tests passed!")


test_breadthFirstSearch()
