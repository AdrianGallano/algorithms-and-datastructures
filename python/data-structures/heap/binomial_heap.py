class MinHeap:
  # for parent of left child i - 1 // 2
  # for parent of right child i - 1 // 2
  # for left child of parent 2(i) + 1
  # for right child of parent 2(i) + 2

  def __init__(self, heap = []):
    self.heap = heap


  def swap(self, a, b):
    temp = self.heap[a]
    self.heap[a] = self.heap[b]
    self.heap[b] = temp

  def swim(self):
    pass

  def sink(self):
    pass

  def insert(self):
    pass

  def remove(self):
    pass

  def poll(self): # also known as popLeft
    pass
  
  def offer(self): # also known as append, or add
    pass

  def heapify(self):
    pass

if __name__ == "__main__":
    pass
