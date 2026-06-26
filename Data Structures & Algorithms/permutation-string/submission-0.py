class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = [0] * 26
        news = [0] * 26
        for i in range(len(s1)):
            arr[ord(s1[i])-ord('a')]+=1
        
        st = 0
        for i in range(len(s2)):
            news[ord(s2[i]) - ord('a')]+=1
            print(tuple(news))
            if tuple(arr) == tuple(news):
                return True
            if i-len(s1)+1 >=0:
                char = s2[i-len(s1)+1]
                news[ord(char) - ord('a')]-=1
        return False