# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tortise and hare algo
        slow = fast = head
        while fast and fast.next: # while there is a fast pointer
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # if fast somehow catches slow, loop
                return True
        
        return False # if no more fast pointer, fast reached an end --> no loop