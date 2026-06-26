class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for p in s:
            if p == ")":
                if not st or st[-1]!= "(":
                    return False
                st.pop()
            elif p == "}":
                if not st or st[-1]!= "{":
                    return False
                st.pop()
            elif p == "]":
                if not st or st[-1]!= "[":
                    return False
                st.pop()
            else:
                st.append(p)
        
        return not st