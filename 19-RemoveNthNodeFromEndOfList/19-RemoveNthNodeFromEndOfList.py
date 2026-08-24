# Last updated: 8/24/2026, 9:52:05 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next # fast is now at the Nth node

        while fast.next:
            fast = fast.next
            slow = slow.next # fast is at last node in list, slow is N nodes away from fast
        
        # now node to delete is 1 pos from right of 'slow' (= slow.next)
        # make current slow point to node after slow.next (skip node to delete)

        slow.next = slow.next.next

        return dummy.next



        