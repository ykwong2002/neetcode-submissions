# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
"""
Goal: Return a boolean on if there is a cycle in the linked list
- use slow and fast pointers
    - slow pointer moves one step each time
    - fast pointer moves two steps each time
    - gap decreases by 1 from fast looping back to slow
- while fast and fast.next both exists
    - keep incrementing them
    - if fast somehow catches slow again, loop exists --> True
1   2   3   4
            s
            f
"""