class Node:
    def __init__(self):
        self.dic = defaultdict(Node)
        self.end = False
class PrefixTree:
        
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.dic[c]
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.dic:
                return False
            cur = cur.dic[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.dic:
                return False
            cur = cur.dic[c]
        return True

        
        