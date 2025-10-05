# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result=[]
        def inOder(Node):
            if not Node :
                return
            inOder(Node.left)
            result.append(Node.val)
            inOder(Node.right)
        inOder(root)
        return result
        