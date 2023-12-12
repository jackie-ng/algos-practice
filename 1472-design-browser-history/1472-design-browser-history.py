class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.cur = self.head

    def visit(self, url: str) -> None:
        newNode = Node(url, None, self.cur)
        self.cur.next = newNode
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            steps -= 1
            self.cur = self.cur.prev
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            steps -= 1
            self.cur = self.cur.next
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)