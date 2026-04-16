# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.maxHeight(root)
    def maxHeight(self,Node):
        if Node is None:
            return 0
        leftNode = self.maxHeight(Node.left)
        rightNode = self.maxHeight(Node.right)
        return 1+max(leftNode,rightNode)

        