# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                NodeP = q1.popleft()
                NodeQ = q2.popleft()

                if NodeP is None and NodeQ is None:
                    continue

                if NodeP is None or NodeQ is None or NodeP.val != NodeQ.val:
                    return False

                q1.append(NodeP.left)
                q1.append(NodeP.right)
                q2.append(NodeQ.left)
                q2.append(NodeQ.right)
        
        return True