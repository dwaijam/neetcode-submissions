class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for c in strs:
            res = res + '#' + str(len(c)) + "$" + c
        return res

    def decode(self, s: str) -> List[str]:
        ret = []
        print(s)
        i = 0
        while i < len(s):
            print(s[i],i)
            if s[i] == '#':
                print("###")
                num = 0
            elif s[i] == "$":
                print("$$$$$$$")
                print(num)
                ret.append(s[i+1:i+1+num])
                print(ret)
                i+=num
            else:
                num = num*10 + int(s[i])
            i+=1

        return ret
