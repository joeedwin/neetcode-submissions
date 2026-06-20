class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []          # tracks current min at each stack level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if min_stack is empty, val is the min; else take the smaller of val vs current min
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()         # keep both in sync

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]    # top of min_stack is always current min