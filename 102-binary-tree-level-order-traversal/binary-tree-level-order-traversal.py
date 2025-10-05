from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []

        def levelNode(Node):
            if not Node:
                return []

            queue = deque([Node])
            while queue:
                level_size = len(queue)
                level_nodes = []

                # Process one level
                for _ in range(level_size):
                    e = queue.popleft()
                    level_nodes.append(e.val)
                    if e.left:
                        queue.append(e.left)
                    if e.right:
                        queue.append(e.right)

                result.append(level_nodes)

        levelNode(root)
        return result
