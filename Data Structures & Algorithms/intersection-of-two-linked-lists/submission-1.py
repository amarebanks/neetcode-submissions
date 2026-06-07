class Solution:
    def getIntersectionNode(self, headA, headB):

        seen = set()

        curr = headA
        while curr:
            seen.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in seen:
                return curr
            curr = curr.next

        return None