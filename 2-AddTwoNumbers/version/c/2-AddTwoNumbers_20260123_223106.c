// Last updated: 1/23/2026, 10:31:06 PM
1struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
2    struct ListNode dummy;
3    struct ListNode* tail = &dummy;
4    dummy.next = NULL;
5
6
7    while (list1 != NULL && list2 != NULL) {
8        if (list1->val <= list2->val) {
9            tail->next = list1;
10            list1 = list1->next;
11        } 
12        else {
13            tail->next = list2;
14            list2 = list2->next;
15        }
16        tail = tail->next;
17    }
18
19    if (list1 != NULL) {
20        tail->next = list1;
21    } else {
22        tail->next = list2;
23    }
24
25    return dummy.next;
26}