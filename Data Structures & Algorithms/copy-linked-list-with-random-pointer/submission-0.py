"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}
        if not head:
            return None
        cur = head
       
        newhead = Node(head.val)
        dic[head] = newhead
        while cur:
            cp = dic.get(cur)
            if cur.random:     
                rc = dic.get(cur.random,  Node(cur.random.val))
                dic[cur.random] = rc
                cp.random = rc
            if cur.next:
                nc = dic.get(cur.next,  Node(cur.next.val))
                dic[cur.next] = nc
                cp.next = nc
            cur = cur.next

        return newhead
        


