class Queue:
    def __init__(self):
        self.storage = []

    def push(self, element):
        self.storage.append(element)

    def peek(self):
        return self.storage[0]

    def pop(self):
        return self.storage.pop(0)

