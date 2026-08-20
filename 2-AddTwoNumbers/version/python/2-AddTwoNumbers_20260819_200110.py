# Last updated: 8/19/2026, 8:01:10 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        num1 = []
9        num2 = []
10
11        curr1 = l1
12        while curr1:
13            num1 += [str(curr1.val)]
14            curr1 = curr1.next
15        
16        curr2 = l2
17        while curr2:
18            num2 += [str(curr2.val)]
19            curr2 = curr2.next
20
21        val1 = int("".join(num1)[::-1])
22        val2 = int("".join(num2)[::-1])
23
24        total_str = str(val1 + val2)[::-1]
25
26        dummy = ListNode(0)
27        curr = dummy
28
29        for char in total_str:
30            curr.next = ListNode(int(char))
31            curr = curr.next
32        
33        return dummy.next