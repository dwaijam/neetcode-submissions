class Node:
    def __init__(self):
        self.dic = defaultdict(Node)
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Node()

        for word in words:
            cur = self.root
            for c in word:
                cur = cur.dic[c]
            cur.word = word
        res = []
        def dfs(r, c,  node)->bool:
            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) or board[r][c] == "_":
                return False
            char = board[r][c]
            board[r][c] = "_"
            ret = False
            if char in node.dic:
                nextNode = node.dic[char]
                if nextNode.word:
                    res.append(nextNode.word)
                    nextNode.word = None
                    ret = True
                    #
                for a,b in (1,0), (-1, 0), (0, 1), (0, -1):
                    ret = dfs(r+a, c+b, nextNode) or ret
            board[r][c] = char
            return ret

        

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, self.root)

        return res