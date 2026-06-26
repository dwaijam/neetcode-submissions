class MinStack:

    def __init__(self):
        self.st = []
        self.ms = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.ms or val <= self.ms[-1]:
            self.ms.append(val)

    def pop(self) -> None:
        p =  self.st.pop()
        if p == self.ms[-1]:
            self.ms.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.ms[-1]
