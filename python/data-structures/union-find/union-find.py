class UnionFind:
    def __init__(self, size):
        assert size > 0, "size should be greater than 0"
        self.components = size
        self.box = []
        self.size = []
        #initialization of the box
        for i in range(size):
            self.box.append(i)
            self.size.append(1)

    def __iter__(self):
        for i in range(len(self.box)):
            yield i
    
    def __repr__(self):
        return "\n".join([f"{x}->{self.box[x]}" for x in self])
    
    def find(self, item): # find the root of the item
        root = item
        while root != self.box[root]:
            root = self.box[root]

        #path compression
        while item != root:
            temp = self.box[item]
            self.box[item] = root
            item = temp
        
        return root

    def connected(self, item1, item2): #if both items have the same parent return connected
        return self.find(item1) == self.find(item2)
    
    def component(self): # returns the total components
        return self.components
    
    def componentSize(self, item): # return the specific size of component
        return self.size[item]

    def unify(self, item1, item2):
        if self.connected(item1,item2):
            return True
        
        root1 = self.find(item1)
        root2 = self.find(item2)

        if self.size[root1] > self.size[root2]:
            self.size[root1] += self.size[root2]
            self.box[root2] = root1
            self.size[root2] = 0
        else:
            self.size[root2] += self.size[root1]
            self.box[root1] = root2
            self.size[root1] = 0
        
        self.components -= 1

if __name__ == "__main__":
    u1 = UnionFind(6)
    u1.unify(0,1)
    u1.unify(2,3)
    u1.unify(3,4)
    u1.unify(0,2)
    u1.unify(0,5)
    print(u1)