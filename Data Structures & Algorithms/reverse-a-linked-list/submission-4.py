# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    

"""
Goal: reverse a linked list (return the head connected to the node before head etc.)
- use stack to store each node and move curr pointer to the end of the list to get tail
- while stack not empty, pop out each node --> O(n) space

instead, use iteration:
- initialise prev = None,  curr = head
    - curr will be used as the main pointer
    - prev will hold the next pointer

    0   1   2   3
p
    c
- use a temp to hold c.next
- c.next = p
- c = temp, p = c

"""