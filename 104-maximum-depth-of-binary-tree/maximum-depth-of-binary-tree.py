# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.maxHeight(root)
    def maxHeight(self,Node):
        if Node is None:
            return 0
        LN=self.maxHeight(Node.left)
        RN=self.maxHeight(Node.right)
        return 1+max(LN,RN)

    