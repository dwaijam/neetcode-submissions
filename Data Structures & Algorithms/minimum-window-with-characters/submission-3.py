class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        freq = defaultdict(int)
        matchlen = 0
        mini = float('inf')
        ans = ""
        st = 0
        for  i in range(len(s)):
            if s[i] in c:
                if freq[s[i]] < c[s[i]]:
                    matchlen+=1
                freq[s[i]]+=1
                
            if matchlen == len(t):
                while st < i and (s[st] not in c or freq[s[st]] > c[s[st]]):
                    if s[st] in c:
                        freq[s[st]]-=1
                    st+=1
                if  i-st+1 < mini:
                    mini = i-st+1
                    ans = s[st:i+1]
                
        
        return ans
                
                        

            

  

    def minWindowD(self, s: str, t: str) -> str:
        c = Counter(t)
        freq = defaultdict(int)
        matchlen = 0
        mini = float('inf')
        ans = ""
        st = 0
        for  i in range(len(s)):
            if s[i] in c:
                if freq[s[i]] == c[s[i]]:
                    while st < i and s[st]!=s[i]:
                        if s[st] in c:
                            c[s[st]]-=1
                            matchlen-=1
                        st+=1
                    st+=1

                else:
                    matchlen+=1
                    freq[s[i]]+=1
            if matchlen == len(t):
                while st < i and s[st] not in c:
                    st+=1
                if  i-st+1 < mini:
                    mini = i-st+1
                    ans = s[st:i+1]
                
        
        return ans
                
                        

            

        