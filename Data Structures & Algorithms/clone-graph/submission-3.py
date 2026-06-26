"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, head: Optional['Node']) -> Optional['Node']:
        if not head:
            return head
        nodes = {}
        visited = set()

        q = deque()
        q.append(head)
        while q:
            pop = q.popleft()
            print("pop",pop.val)

            node = nodes.get(pop, Node())
            nodes[pop] = node
            node.val = pop.val
            for nei in pop.neighbors:
                print(nei.val)
                if nei not in nodes:
                    q.append(nei)
                nn = nodes.get(nei, Node())
                nodes[nei] = nn
                node.neighbors.append(nn)
                

            visited.add(pop)
        
        return nodes[head]

            

        