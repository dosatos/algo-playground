class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def _in_order(root):
    if root is not None:
        _in_order(root.left)
        if root.data:
            print(root.data, end=" ")
        _in_order(root.right)


def _pre_order(root):
    if root is not None:
        if root.data:
            print(root.data, end=" ")
        _pre_order(root.left)
        _pre_order(root.right)


def _post_order(root):
    if root is not None:
        _pre_order(root.left)
        _pre_order(root.right)
        if root.data:
            print(root.data, end=" ")


def _insert_level_order(arr, root, i, n):
    if i >= n:
        # return root
        return

    _root = Node(arr[i])
    _root.left = _insert_level_order(arr, _root.left, 2 * i + 1, n)
    _root.right = _insert_level_order(arr, _root.right, 2 * i + 2, n)
    return _root


"""
                1
             /     \
        None           3
                     /   \
                    4     None
                  /  \
                 5   None
               /   \
              6     7
"""
if __name__ == '__main__':
    arr = [1, None, 3, 4, None, 5, None, 6, 7]
    arr = [1, None, 3, 4]
    # arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = _insert_level_order(arr, root, 0, n)
    _in_order(root)
    print()
    _pre_order(root)
    print()
    _post_order(root)
    print()
