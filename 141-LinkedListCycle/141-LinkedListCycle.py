# Last updated: 9/2/2026, 2:31:01 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head # first node in list
        seen = set()

        while curr:
            if curr in seen:
                return True

            seen.add(curr)
            curr = curr.next


        return False