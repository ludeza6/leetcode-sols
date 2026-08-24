# Last updated: 8/24/2026, 9:52:08 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []

        curr1 = l1
        while curr1:
            num1 += [str(curr1.val)]
            curr1 = curr1.next
        
        curr2 = l2
        while curr2:
            num2 += [str(curr2.val)]
            curr2 = curr2.next

        val1 = int("".join(num1)[::-1])
        val2 = int("".join(num2)[::-1])

        total_str = str(val1 + val2)[::-1]

        dummy = ListNode(0)
        curr = dummy

        for char in total_str:
            curr.next = ListNode(int(char))
            curr = curr.next
        
        return dummy.next