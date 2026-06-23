# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            curr = queue.pop()
            if curr.val == subRoot.val:
                if self.isSame(curr, subRoot):
                    return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return False

    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
