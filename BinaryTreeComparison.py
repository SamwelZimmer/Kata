class BinaryNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def compare(a: BinaryNode, b: BinaryNode):

    # base case: if both are the same -> structural check
    if not a and not b:
        return True

    # base case: no longer equal -> structural check
    if not a or not b:
        return False

    # base case: values are not the same -> value check
    if a.value != b.value:
        return False

    return compare(a.left, b.left) and compare(a.right, b.right)
