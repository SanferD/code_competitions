"""Find the path with the maximum sum
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):

    # initial max sum
    (max_sum, max_path) = (float("-inf"), None)

    # dictionary to keep remember max paths
    node2max = dict()

    # figure out the maximum path recursively
    def helper(node):
        nonlocal max_sum, max_path

        # the idea is that there are four ways the max path can go through current node
        # -node
        # -node + lt
        # -node + rt
        # -lt + node + rt
        # the max path of those four is the max path that goes through the current node

        # base case: empty tree => empty path
        if node is None:
            return (0, [])

        # base case: we already did this node
        if node.val in node2max:
            return node2max[id(node)]

        #~
        # infer the maximum sum and corresponding path for current node

        # get the max sum and max paths of left and right subtrees
        (left_max_sum, left_max_path) = helper(node.left)
        (right_max_sum, right_max_path) = helper(node.right)

        # initialize to current node
        (node_sum, node_path) = (node.val, [node.val])

        # update if node+lt is max node path
        if node.val + left_max_sum > node_sum:
            (node_sum, node_path) = (node.val + left_max_sum, left_max_path + [node.val])

        # update if node+rt is max node path
        if node.val + right_max_sum > node_sum:
            (node_sum, node_path) = (node.val + right_max_sum, [node.val] + right_max_path)

        # update the max sum/path if this is the max
        if node_sum > max_sum:
            (max_sum, max_path) = (node_sum, node_path)

        # update the max path if it contains the entire path
        if left_max_sum + node.val + right_max_sum > max_sum:
            max_sum = left_max_sum + node.val + right_max_sum
            max_path = left_max_path + [node.val] + right_max_path

        # update the dictionary
        node2max[id(node)] = (node_sum, node_path)
        return (node_sum, node_path)

    helper(root)
    #print( " -> ".join(map(str, max_path)) )
    return max_sum


if __name__ == "__main__":
    # Driver program
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right   = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.right = None
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    print("Max path sum is " ,max_path_sum(root))

