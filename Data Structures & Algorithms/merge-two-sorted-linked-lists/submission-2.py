# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val: # list1 is next
                dummy.next = list1
                list1 = list1.next
            else: # list2 is next
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        dummy.next = list1 or list2 # will chain whichever list still has remainders

        return head.next
            
"""
Goal: merge 2 sorted linked lists into 1 sorted linked list
- at each stage, compare the curr pointer of both
- add the smaller one to the new linked list, shift the pointer for that linked list
- if reach end of the linked list, simply point to the other linked list

1   2   4
            c
1   3   5
        c

1   1   2   3   4   
"""