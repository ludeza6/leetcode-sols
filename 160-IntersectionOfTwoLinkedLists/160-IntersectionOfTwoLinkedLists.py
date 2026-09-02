# Last updated: 9/2/2026, 2:31:12 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seenA = set()
        currA = headA

        while currA:
            seenA.add(currA)
            currA = currA.next
        
        currB = headB

        while currB:
            if currB in seenA:
                return currB
            currB = currB.next
        return None