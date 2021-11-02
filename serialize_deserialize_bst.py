"""Serialize and deserialize bst
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize_bst(root):
    values = []
    def preorder(node):
        if node is None:
            return
        values.append(node.val)
        preorder(node.left)
        preorder(node.right)
    return ",".join(map(str,values))


def deserialize_bst(data):
    # extract preorder
    preorder = [int(x) for x in data.split(",")] 

    # base case: empty preorder
    if len(preorder) == 0:
        return None

    # helper function 
    def helper(min_i, max_i):

        # base case: empty preorder
        if len(preorder) == 0:
            return None

        # if candidate value is within interval, recursively build next level
        if min_i < preorder[0] < max_i:

            # initialize the node
            val = preorder.pop(0)
            node = TreeNode(val)

            # recursively build left st
            node.left = helper(min_i, val)

            # recursively build right st
            node.right = helper(val, max_i)

        # candidate value is not in subtree
        else:
            node = None

        # return the node
        return node

    # initial call
    return helper(float("-inf"), float("inf"))


if __name__ == "__main__":
    s = "10,5,1,7,40,50"
    r = deserialize_bst(s)
    values = []
    def preorder(n):
        if n is None:
            return
        values.append(n.val)
        preorder(n.left)
        preorder(n.right)
    preorder(r)
    print(",".join(map(str, values)))


