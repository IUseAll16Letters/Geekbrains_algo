

class Queue:
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.queue = [None] * size
        self.size = 0
        self.max_size = size

    def is_empty(self):
        return not self.size

    def push(self, value):
        if self.size < self.max_size:
            print('tail: ', self.tail, end=' after: ')
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
            print(self.tail)
        else:
            print('Queue is full')

    def pop(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        print('head: ', self.head, end=' after: ' )
        self.head = (self.head + 1) % self.max_size
        print(self.head)
        self.size -= 1
        return item

    def __iter__(self):
        for item in self.queue[self.head:]:
            if item is not None:
                yield item
        for item in self.queue[:self.head]:
            if item is not None:
                yield item

    def __str__(self):
        values = []
        for i in self:
            values.append(i)
        return ', '.join(values)

    def peek(self): return self.queue[self.head]
    def size(self): return self.size


if __name__ == '__main__':
    queue_ = Queue(4)
    queue_.push('Apple')
    print(queue_.queue)
    queue_.push('Banana')
    queue_.push('Citron')
    queue_.push('Debil')
    print(queue_)

    queue_.pop()

    queue_.push('France')
    print(queue_)
