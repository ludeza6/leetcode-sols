# Last updated: 8/24/2026, 9:51:00 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        dummy = ListNode(0, head)
9        fast = dummy
10        slow = dummy
11
12        for _ in range(n):
13            fast = fast.next # fast is now at the Nth node
14
15        while fast.next:
16            fast = fast.next
17            slow = slow.next # fast is at last node in list, slow is N nodes away from fast
18        
19        # now node to delete is 1 pos from right of 'slow' (= slow.next)
20        # make current slow point to node after slow.next (skip node to delete)
21
22        slow.next = slow.next.next
23
24        return dummy.next
25
26
27
28        