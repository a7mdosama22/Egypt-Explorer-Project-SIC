class NavigationStack:
    def __init__(self):
        self.stack = []

    def push(self, page):
        self.stack.append(page)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def back(self):
        if len(self.stack) > 1:
            self.stack.pop()
            return self.stack[-1]
        return None