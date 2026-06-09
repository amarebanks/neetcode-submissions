# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        if not root:
            return None

        queue = deque([root])

        while queue:
            Node = queue.popleft()
            Node.left, Node.right = Node.right, Node.left
            if Node.right:
                queue.append(Node.right)
            if Node.left:
                queue.append(Node.left)



        return root
        