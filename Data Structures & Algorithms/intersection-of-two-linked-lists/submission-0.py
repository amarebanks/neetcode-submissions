class Solution:
    def getIntersectionNode(self, headA, headB):

        arr1 = []
        arr2 = []

        curr1 = headA
        curr2 = headB

        while curr1:
            arr1.append(curr1)
            curr1 = curr1.next

        while curr2:
            arr2.append(curr2)
            curr2 = curr2.next

        node_set = set(arr1)

        for node in arr2:
            if node in node_set:
                return node

        return None