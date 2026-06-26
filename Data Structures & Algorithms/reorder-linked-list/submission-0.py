# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            cur = head
            prev = None
            while cur:
                nex = cur.next
                cur.next = prev
                prev = cur
                cur = nex
            return prev

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        newhead = reverse(slow.next)
        slow.next = None
        cur = head
        newCur = newhead
        while newCur:
            nex = cur.next
            newNex = newCur.next
            cur.next = newCur
            newCur.next = nex
            cur = nex
            newCur = newNex