"""Serialize and deserialize generic binary tree
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):

    # list of values
    values = []

    # helper function for preorder traversal
    def preorder(node):
        if node is None:
            values.append("")
        else:
            values.append(node.val)
            preorder(node.left)
            preorder(node.right)

    # populate values via preorder + | + inorder
    preorder(root)

    # build string with "," as delim
    return ",".join(map(str, values))


def deserialize(data):

    # parse preorder and inorder
    parse = lambda x: None if len(x) == 0 else int(x)
    preorder = [parse(x) for x in data.split(",")]

    #~
    # build the tree

    # helper function to build the tree
    def helper():

        # base case: empty preorder
        if len(preorder) == 0:
            return None

        # get the val
        val = preorder.pop(0)

        # base case: value is null sentinel
        if val is None:
            return None

        # initialize with value
        node = TreeNode(val)

        # recursively build left subtree
        node.left = helper()

        # recursively build right subtree
        node.right = helper()

        # return the tree
        return node

    # actually construct the tree via helper
    return helper()


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    s = serialize(root)
    print(s)
    r = deserialize(s)
    values = []
    def preorder(node):
        if node is None:
            return
        values.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(r)
    print(",".join(map(str, values)))

