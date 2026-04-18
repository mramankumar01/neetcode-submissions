class MyQueue:

    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def transfer(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def pop(self) -> int:
        self.transfer()
        return self.outbox.pop()

    def peek(self) -> int:
        self.transfer()
        return self.outbox[-1]

    def empty(self) -> bool:
        return not self.inbox and not self.outbox


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()