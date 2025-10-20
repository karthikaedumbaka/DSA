# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minNodeVal(self,root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # 1st case 0 or 1 child
        # 2nd cal 2 child
        if not root:
            return None
        if key > root.val :
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minval = self.minNodeVal(root.right)
                root.val = minval.val
                root.right = self.deleteNode(root.right,minval.val)
        return root
        