# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def preOder(Node):
            if not Node:
                return
            result.append(Node.val)
            preOder(Node.left)
            preOder(Node.right)
        preOder(root)

        return result
        