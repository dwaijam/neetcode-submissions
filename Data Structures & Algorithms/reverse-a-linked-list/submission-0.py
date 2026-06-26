# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        after = head.next
        while after.next:
            newafter = after.next
            after.next = cur
            cur = after
            after = newafter
        
        after.next = cur
        head.next = None
        return after
