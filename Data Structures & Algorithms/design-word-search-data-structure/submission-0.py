class Node:
    def __init__(self):
        self.dic = defaultdict(Node)
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.dic[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        return self.helper(word, 0, self.root)
    
    def helper(self, word: str, i: int, cur: Node):
        print(word, i)
        print (cur.end)
        print (cur.dic)
        if i == len(word):
            return cur.end
        char = word[i]
        if char == '.':
            for node in cur.dic.values():
                if self.helper(word, i+1, node):
                    return True
            return False
        else:
            if char in cur.dic:
                return self.helper(word, i+1, cur.dic[char])
            else:
                return False
        


        
        
