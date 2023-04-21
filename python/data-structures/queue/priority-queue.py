class MinPriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, n):
        assert type(n) == int
        self.queue.append(n)

    def dequeue(self):
        if not self.queue:
            raise OverflowError

        data = min(self.queue)
        self.queue.remove(data)
        return data
    
    def __repr__(self):
        return str(self.queue)


class MaxPriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, n):
        assert type(n) == int
        self.queue.append(n)

    def dequeue(self):
        if not self.queue:
            raise OverflowError

        data = max(self.queue)
        self.queue.remove(data)
        return data

    def __repr__(self):
        return str(self.queue)

if __name__ == "__main__":
    minPQ = MinPriorityQueue()
    maxPQ = MaxPriorityQueue()

    minPQ.enqueue(6)
    minPQ.enqueue(8)
    minPQ.enqueue(7)
    minPQ.dequeue()
    minPQ.dequeue()
    print(minPQ)


    maxPQ.enqueue(6)
    maxPQ.enqueue(8)
    maxPQ.enqueue(7)
    maxPQ.dequeue()
    maxPQ.dequeue()
    print(maxPQ)