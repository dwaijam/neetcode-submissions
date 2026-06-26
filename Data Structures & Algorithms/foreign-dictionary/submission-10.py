class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dic = {c:set() for w in words for c in w}
        for i in range(1, len(words)):
            l = min(len(words[i]), len(words[i-1]))
            if len(words[i-1]) > len(words[i]) and words[i-1][:l] == words[i][:l]:
                return ""
            for j in range(l):
                if words[i-1][j]!=words[i][j]:
                    dic[words[i-1][j]].add(words[i][j])
                    break

        res = []
        color = {k : 0 for k in dic.keys()}
        #print(dic)
        def dfs(c)->bool:
            if color[c] == 1:  # GRAY → Cycle detected
                return True
            if color[c] == 2:  # BLACK → Already processed
                return False

            color[c]=1
            for neighbor in dic.get(c, []):
                if dfs(neighbor):
                    return True
            color[c]=2
            res.append(c)
            return False
        
        print(dic)
        print(color)

        for c in dic:
            if color[c] == 0:
                if dfs(c):
                    return ""
        
        return ''.join(res[::-1])
            




        
