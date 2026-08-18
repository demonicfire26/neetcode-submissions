class MinStack:

    def __init__(self):
        self.stack = []          # Main stack to store values
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or val is smaller/equal to current min, push to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            # If popped value is the same as current min, pop from min_stack too
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
