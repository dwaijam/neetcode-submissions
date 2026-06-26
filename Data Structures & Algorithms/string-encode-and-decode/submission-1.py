class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for c in strs:
            res = res + '#' + str(len(c)) + "$" + c
        return res

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            print(s[i],i)
            if s[i] == '#':
                num = 0
            elif s[i] == "$":
                ret.append(s[i+1:i+1+num])
                i+=num
            else:
                num = num*10 + int(s[i])
            i+=1

        return ret
