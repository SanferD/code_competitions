"""Construct binary tree from postorder and inorder traversal
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


def construct(inorder, postorder):

    # build dict of inorder indexes
    inorder_indexes = dict()
    for (i, x) in enumerate(inorder):
        inorder_indexes[x] = i

    def helper(inorder_beg, inorder_end, postorder_beg, postorder_end):

        # empty postorder => null tree
        if postorder_beg >= postorder_end:
            return None

        # last element of postorder is root node
        # get the root node
        root = postorder[postorder_end - 1]

        # find the corresponding element's index in inorder
        i = inorder_indexes[root]

        # implicilty split inorder about the found index
        # do this by using the lengths of the left and right split
        L_left = i - inorder_beg
        L_right = inorder_end - i - 1

        # initialize node
        node = TreeNode(root)

        # build right subtree using
        # -indexes for right split of inorder, computed via splice [inorder_end-L_right, inorder_end)
        # -indexes for right split of postorder, computed via splice [postorder_end-L_right-1, postorder_end-1)
        node.right = helper(inorder_beg=inorder_end-L_right, inorder_end=inorder_end,
                            postorder_beg=postorder_end-L_right-1, postorder_end=postorder_end-1)

        # build left subtree using
        # -indexes for left split of inorder, computed via splice [inorder_beg, inorder_beg+L_left)
        # -indexes for left split of postorder, computed via splice [postorder_beg, postorder_beg+L_left)
        node.left = helper(inorder_beg=inorder_beg, inorder_end=inorder_beg+L_left,
                            postorder_beg=postorder_beg, postorder_end=postorder_beg+L_left)

        # return node
        return node

    # construct with helper
    return helper(inorder_beg=0, inorder_end=len(inorder), postorder_beg=0, postorder_end=len(postorder))


if __name__ == "__main__":
    PREORDER = "preorder"
    INORDER = "inorder"
    POSTORDER = "postorder"

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
            if kind == POSTORDER:
                values.append(n.val)
        helper(tree)
        return values
    
    test_cases = [
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]),
    ]
    for (inorder, postorder) in test_cases:
        tree = construct(inorder, postorder)
        found_inorder = traverse(INORDER, tree)
        found_postorder = traverse(POSTORDER, tree)
        assert found_inorder == inorder, f"inorder: desired={inorder}, found={found_inorder}"
        assert found_postorder == postorder, f"inorder: desired={postorder}, found={found_postorder}"

