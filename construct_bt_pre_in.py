"""Construct a binary tree from preorder and inorder traversal.
"""


class TreeNode:
    """Datastructure that represents a node in a binary tree.

    Args
    ====
    val: any
        The data in the node
    left: Union[node, None], optional
        The left node, or None if no such node
    right: Union[node, None], optional
        The right node, or None if no such node
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct(preorder, inorder):

    # build dict of indexes
    inorder_indexes = dict()
    for (i, n) in enumerate(inorder):
        inorder_indexes[n] = i

    # helper function that will build the tree recursively given the intervals
    # [preorder_beg, preorder_end)
    # [inorder_beg, inorder_end)
    def helper(preorder_beg, preorder_end, inorder_beg, inorder_end):

        # preorder indexes out-of-bounds => empty tree 
        if preorder_beg >= preorder_end:
            return None

        # extract root of tree
        root = preorder[preorder_beg]
        preorder_beg += 1

        # split inorder around tree node
        # this will be (list of left nodes, list of right nodes)
        i = inorder_indexes[root]

        # initialize the node
        node = TreeNode(root)

        # compute the length of the left inorder subtree
        L_left = i - inorder_beg 
        L_right = inorder_end - i - 1

        # build the left tree
        node.left = helper(preorder_beg=preorder_beg, preorder_end=preorder_beg+L_left,
                           inorder_beg=inorder_beg, inorder_end=inorder_beg+L_left)

        # buld the right tree
        node.right = helper(preorder_beg=preorder_beg+L_left, preorder_end=preorder_beg+L_left+L_right,
                            inorder_beg=inorder_end-L_right, inorder_end=inorder_end)

        # return the built node
        return node

    return helper(preorder_beg=0, preorder_end=len(preorder),
                  inorder_beg=0, inorder_end=len(inorder))


if __name__ == "__main__":
    PREORDER = "preorder"
    INORDER = "inorder"
    def traverse(kind, tree):
        values = []
        def helper(n):
            nonlocal values
            if n is None:
                return
            if kind == PREORDER:
                values.append(n.val)
            helper(n.left)
            if kind == INORDER:
                values.append(n.val)
            helper(n.right)
        helper(tree)
        return values
    
    test_cases = [
        ([1, 2, 4, 5, 3], [4, 2, 5, 1, 3]),
    ]

    for (preorder, inorder) in test_cases:
        tree = construct(preorder, inorder)
        found_preorder = traverse(PREORDER, tree)
        found_inorder = traverse(INORDER, tree)
        assert found_preorder == preorder, f"preorder: desired={preorder}, found={found_preorder}"
        assert found_inorder == inorder, f"inorder: desired={inorder}, found={found_inorder}"

