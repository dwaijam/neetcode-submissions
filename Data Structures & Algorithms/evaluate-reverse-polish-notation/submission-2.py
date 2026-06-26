class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        st = []
        res = 0
        for tok in tokens:
            if tok in {"+", "-", "*", "/"}:
                b = st.pop()
                a = st.pop()
                res = operations[tok](a,b)
                st.append(res)
            else:
                st.append(int(tok))
        
        return st[0]

