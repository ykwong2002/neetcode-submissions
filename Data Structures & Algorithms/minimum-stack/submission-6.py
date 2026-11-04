class MinStack:

    def __init__(self):
        self.main = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.main.append(val)
        val = min(val, self.smallest[-1] if self.smallest else val)
        self.smallest.append(val)

    def pop(self) -> None:
        self.main = self.main[:-1]
        self.smallest = self.smallest[:-1]

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.smallest[-1]
"""
Goal: implement stack with all O(1) functions, including getMin
- use a second stack that corresponds with minimum at each level
main    1   2   0
min       1   1   0
"""