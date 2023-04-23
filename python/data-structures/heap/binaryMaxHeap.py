def UnderflowError(Exception):
  pass

class MaxHeap:
  # left child is odd
  # right child is even
  # for parent of left child i - 1 // 2 
  # for parent of right child i - 2 // 2
  # for left child of parent 2(i) + 1
  # for right child of parent 2(i) + 2

  def __init__(self, heap = []):
    self.heap = heap

  def __repr__(self):
    return str(self.heap)

  def getParent(self, i):
    return (i-1) // 2 if i % 2 != 0 else (i-2) // 2

  def getBiggerChild(self, left, right):
    if right <= len(self.heap) - 1:
      return left if self.heap[left] > self.heap[right] else right
    elif left == len(self.heap) - 1:
      return left
    else:
      return None

  def getLeftChild(self, i):
      return 2 * i + 1

  def getRightChild(self, i ):
      return 2 * i + 2

  def swap(self, a, b):
    temp = self.heap[a]
    self.heap[a] = self.heap[b]
    self.heap[b] = temp

  def swim(self, i):
    parent = self.getParent(i)# determine if left or right

    while(self.heap[i] > self.heap[parent] and i > 0): # swim while current node is greater than parent
      self.swap(i, parent)
      i = parent
      parent = (i-1) // 2 if i % 2 != 0 else (i-2) // 2

  def sink(self, i):
    child = self.getBiggerChild(self.getLeftChild(i), self.getRightChild(i))
    while child != None and self.heap[child] > self.heap[i]:
      self.swap(i,child)
      i = child
      child = self.getBiggerChild(self.getLeftChild(i), self.getRightChild(i))

  def poll(self): # also known as popLeft
    if len(self.heap) == 0:
      raise UnderflowError
    self.swap(0, len(self.heap) - 1)
    r = self.heap.pop()
    self.sink(0)
    return r

  def offer(self,num): # also known as append, or add
    self.heap.append(num)
    self.swim(len(self.heap) - 1)


  def remove(self, n):
    if len(self.heap) == 0:
      raise UnderflowError

    i = self.traverse(n)
    if i == None:
      return None

    self.swap(i, len(self.heap) - 1)
    self.heap.pop()
    if self.heap[self.getParent(i)] < self.heap[i]:
      self.swim(i)
    elif self.heap[self.getBiggerChild(self.getLeftChild(i), self.getRightChild(i))] > self.heap[i]:
      self.sink(i)
    else:
      pass

  def traverse(self, n):
    for i in range(len(self.heap)):
      if self.heap[i] == n:
        return i 
    return None

  def heapify(self):
    pass

if __name__ == "__main__":
    mHeap = MaxHeap()
  
    mHeap.offer(20)
    mHeap.offer(17)
    mHeap.offer(13)
    mHeap.offer(19)
    mHeap.offer(2)
    mHeap.offer(5)
    mHeap.offer(6)
    mHeap.offer(9)
    mHeap.offer(10) 
    mHeap.offer(10)
    mHeap.offer(12)
    print(mHeap)
    mHeap.poll()
    print(mHeap)

    # print(mHeap)
    # mHeap.remove(12)
    # print(mHeap)
    # mHeap.remove(19)
    # print(mHeap)