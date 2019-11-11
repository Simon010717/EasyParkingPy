class ListNode:
    def __init__ (self, data, next):
        self.data = data
        self.next = next
    
class LinearList:
    def __init__ (self):
        self.front = None
        self.size = 0
    
    def isEmpty(self):
        return size == 0
    
    def getFront(self):
        return front.data
    
    def get (self, index):
        if index >= size or index<0: return None
        currentNode = self.head
        for i in range (index):
            currentNode = currentNode.next
        return currentNode.data
    
    def indexOf(self, data):
        currentNode = self.head
        index = 0
        while (currentNode is not None and currentNode.data != data):
            currentNode = currentNode.next
            index += 1
        if currentNode is None:
            return -1
        else:
            return index
    
    def remove(self,index):
        if index >= size or index<0: return None
        removed = None
        if index == 0:
            removed = self.head.data
            self.head = self.head.next
        else:
            q = self.head
            for i in range(index-1): q = q.next
            removed = q.next.data
            q.next = q.next.next
        self.size -= 1
        return removed
    
    def add(self, index, data):
        if index<0 or index>size: return None
        if index == 0: self.head = ListNode(data,self.head)
        else:
            q = self.head
            for i in range(index-1): q = q.next
            q.next = ListNode(data,q.next)
        size += 1
        return True
    
    def toString(self):
        print("[",end="")
        q = self.head
        for i in range (size-1):
            print(q.data,end=",")
            q = q.next
        print(q.data + "]",end="")

class Stack(LinearList):

    def __init__(self):
        LinearList.__init__()
    
    def isEmpty(self):
        return super().isEmpty()
    
    def peek(self):
        if (self.isEmpty()): return None
        return self.get(0)
    
    def push(self,data):
        self.add(0,data)
    
    def pop(self):
        if (self.isEmpty): return None
        return self.remove(0)

class Queue():

    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self):
        return self.front is None
    
    def peekFront(self):
        if(self.isEmpty()): return None
        return self.front.data
    
    def queue(self,data):
        q = ListNode(data,None) 
        if(self.isEmpty()): self.front = q
        else: self.back.next = q
        self.back  = q

    def dequeue(self):
        if self.isEmpty(): return None
        frontData = self.front.data
        self.front = self.front.next
        if self.isEmpty(): self.back = None
        return frontData
    
class BinarySearchTree:
    
    class BinaryNode:
        def __init__ (self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__ (self):
        self.root = None

    def makeEmpty(self):
        self.root = None
    
    def isEmpty(self):
        return root is None
    
    def insert(self, x, t):
        if t is None: return BinaryNode(x)
        if x > t.data: t.right = self.insert(x,t.right)
        if x < t.data: t.left = self.insert(x,t.left)

        return t

    def contains(self,x,t):
        if t is None: return False
        if x == t.data: return True
        if x > t.data: return self.contains(x,t.right)
        if x < t.data: return self.contains(x,t.left)

    def remove(self,x,t):
        if t is None: return t
        if x > t.data: t.right = self.remove(x,t.right)
        elif x < t.data: t.left = self.remove(x,t.left)
        elif t.right is not None and t.left is not None:
            t.data = self.findMax(t.right)
            r.right = t.remove(t.data,t.right)
        else:
            if t.left is None: return t.right
            else: return t.left
    
    def findMin(self,t):
        if t.left is None: return t.data
        else: return self.findMin(t.left)

    def findMax(self,t):
        if t.right is None: return t.data
        else: return self.findMax(t.right)

    def height(self,t):
        if t is None: return 0
        if t.left is None and t.right is None: return 1
        elif t.left is None: return self.height(t.right)+1
        elif t.right is None: return self.height(t.left)+1
        else: return max(self.height(t.right),self.height(t.left))

    def inOrder(self,t):
        if t is None: return 
        if t.left is not None: self.inOrder(t.left)
        print(t.data,end = ',')
        if t.right is not None: self.inOrder(t.right)
    
class AvlTree(BinarySearchTree):

    class AvlNode:
        def __init__(self):
            self.data = None
            self.left = None
            self.right = None
            self.height = 0

    def __init__(self):
        self.root = None
    
    def singleRotationR(self,t):
        temp = t.left
        t.left = temp.right
        temp.right = t
        t = temp
        return t

    def singleRotationL(self,t):
        temp = t.right
        t.right = temp.left
        temp.left = t
        t = temp
        return t

    def rotationLR(self,t):
        t.right = self.singleRotationL(t.right)
        t = self.singleRotationR(t)
        return t
    
    def rotationRL(self,t):
        t.left = self.singleRotationR(t.left)
        t = self.singleRotationL(t)
        return t

    def insert(self, x, t):
        if t is None:
            t = self.AvlNode()
            t.data = x
            t.height = 1
        if x == t.data:
            return t
        elif x < t.data:
            t.left =  self.insert(x,t.left)
            if super().height(t.left) - super().height(t.right) == 2:
                if x < t.left.data: t = self.singleRotationR(t)
                else: t = self.rotationLR(t)
        elif x > t.data: 
            t.right = self.insert(x,t.right)
            if super().height(t.right) - super().height(t.left) == 2:
                if x >  t.right.data: t = self.singleRotationL(t)
                else: t = self.rotationRL(t)
        t.height = max(super().height(t.left),super().height(t.right)) + 1
        return t
    
    def remove(self,x,t):
        if t is None: return None
        if x > t.data: 
            t.right = self.remove(x,t.right)
            if super().height(t.left) - super().height(t.right) == 2:
                if x < t.left.data: t = self.singleRotationR(t)
                else: t = self.rotationLR(t)
        elif  x < t.data:
            t.left = self.remove(x,t.left)
            if super().height(t.right) - super().height(t.left) == 2:
                if x >  t.right.data: t = self.singleRotationL(t)
                else: t = self.rotationRL(t)
        elif t.right is not None and t.left is not None:
            t.data = self.findMax(t.right)
            t.right = self.remove(t.data,t.right)
        else:
            if t.left is None:
                return t.right
            else:
                return t.left
        t.height = max(super().height(t.left),super().height) + 1
        return t

    def siguiente(self,x,n):
        if x<1 or x>n: return None
        s = 0
        k = 0
        while s + pow(2,k) < x:
            s += pow(2,k)  
            k+=1
        if not self.contains(int(n*(2*(x-s)-1)/pow(2,k+1)),self.root):
            return int(n*(2*(x-s)-1)/pow(2,k+1))
        else:
            return self.siguiente(x-1,n)

    def siguienteLibre(self,x,n):
        siguiente = self.siguiente(x,n)        
        if siguiente is not None:
            return siguiente
        else:
            k = n-1
            while self.contains(k,self.root):
                k -= 1
            return k
'''
class ObjAvlTree:
    def __init__(self,capacity):
        self.tree = [None]*capacity
        self.capacity = capacity
    

    def _left(self,n):
        return 2*n
    
    def _right(self,n):
        return 2*n+1


    def singleRotationR(self,x):
        print("RR")
        temp = self._left(x)
        self.tree[self._left(x)] = self.tree[self._right(temp)]
        self.tree[self._right(temp)] = self.tree[x]
        self.tree[x] = self.tree[temp]
        return x

    def singleRotationL(self,x):
        print(f"LL {x}")
        print(self.tree)
        temp = self.tree[self._right(x)]
        self.tree[self._right(x)] = self.tree[self._left(temp)]
        self.tree[self._left(temp)] = self.tree[x]
        self.tree[x] = self.tree[temp]
        print(self.tree)
        return x

    def rotationLR(self,x):
        self.singleRotationL(self._right(x))
        self.singleRotationR(x)
        return x
    
    def rotationRL(self,x):
        self.singleRotationR(self._left(x))
        self.singleRotationL(x)
        return x

    def insert(self, val, obj, x):
        if x >= self.capacity or x < 1: return -1 
        if self.tree[x] is None:
            self.tree[x] = [val,obj,1]
        if val == self.tree[x][0]:
            return x
        elif val < self.tree[x][0]:
            self.insert(val,obj,self._left(x))
            if self.height(self._left(x)) - self.height(self._right(x))  == 2:
                print(f"Rot l{self.height(self._left(x))}  r{self.height(self._right(x))}")
                if val < self.tree[self._left(x)][0]: self.singleRotationR(x)
                else: self.rotationLR(x)
        elif val > self.tree[x][0]: 
            self.insert(val,obj,self._right(x))
            if self.height(self._right(x)) - self.height(self._left(x))  == 2:
                print(f"Rot l{self.height(self._left(x))}  r{self.height(self._right(x))}")
                if val > self.tree[self._right(x)][0]: self.singleRotationL(x)
                else: self.rotationRL(x)
        print(f"try {x}")
        self.tree[x][2] = max(self.height(self._right(x)),self.height(self._left(x))) + 1
        print(self.tree)
        return x
    
    def remove(self,val,x):
        if x >= self.capacity or x < 1: return -1
        if self.tree[x] is None: return -1
        elif val > self.tree[x][0]: 
            self.remove(x,val,self._right(x))
            if self.height(self._left(x)) - self.height(self._right(x))  == 2:
                if val < self.tree[self._left(x)][0]: self.singleRotationR(x)
                else: self.rotationLR(x)
        elif  val < self.tree[x][0]:
            self.remove(x,val,self._left(x))
            if self.height(self._right(x)) - self.height(self._left(x))  == 2:
                if val > self.tree[self._right(x)][0]: self.singleRotationL(x)
                else: self.rotationRL(x)
        elif self.tree[self._right(x)] is not None and self.tree[self._left(x)] is not None:
            m = self.findMax(self._right(x))
            self.tree[x] = [self.tree[m][0],self.tree[m][1],0]
            self.remove(self.tree[self._right(x)][0],self._right(x))
        else:
            if self.tree[self._left(x)] is None:
                return self._right(x)
            else:
                return self._left(x)
        self.tree[x][2] = max(self.height(self._right(x)),self.height(self._left(x))) + 1
        return x

    def findMin(self,x):
        if self.tree[self._left(x)] is None: return x
        else: return self.findMin(self._left(x))

    def findMax(self,x):
        if self.tree[self._right(x)] is None: return x
        else: return self.findMax(self._right(x))

    def height(self,x):
        if self.tree[x] is None: return 0
        if self.tree[self._left(x)] is None and self.tree[self._right(x)] is None: return 1
        elif self.tree[self._left(x)] is None: return self.height(self._right(x))+1
        elif self.tree[self._right(x)] is None: return self.height(self._left(x))+1
        else: return max(self.height(self._right(x)),self.height(self._left(x))) + 1
'''
class BinaryHeap():
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.heap = [None]*capacity

    def insert(self,x):
        if self.size == self.capacity - 1: return False
        #sift up
        sp = self.size + 1
        while x.priority < self.heap[int(sp/2)].priority:
            self.heap[sp] = self.heap[int(sp/2)]
            sp = int(sp/2)
        
        self.heap[sp] = x

    def findMin(self):
        if size > 0: return self.heap[1]
        
    def deleteMin(self):
        if size < 0: return None

        min = self.findMin()

        self.heap[1] = self.heap[self.size-1]
        self.size -= 1

        #sift down
        hole = 1
        tmp = self.heap[1]
        while hole*2 < self.size:
            child = hole*2

            if child != self.size and self.heap[child].priority > self.heap[child+1].priority: child +=1
            if self.heap[child] < tmp: self.heap[hole] = self.heap.child
            else: break

        self.heap[hole] = tmp

