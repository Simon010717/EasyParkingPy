import random

class ListNode:
    def __init__ (self, data, next):
        self.data = data
        self.next = next
    
class LinearList:
    def __init__ (self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return size == 0
    
    def getFront(self):
        return self.head.data
    
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
        for i in range (self.size-1):
            print(q.data,end=",")
            q = q.next
        print(str(q.data) + "]")

class OrderedList(LinearList):
    def __init__(self):
        LinearList.__init__(self)
        self.middle = None

    def add(self, data):
        if self.size == 0 or data < self.head.data:
            self.head = ListNode(data,self.head)
        else:
            q = self.head           
            while q.next is not None and data > q.next.data:
                q = q.next
            q.next = ListNode(data,q.next)
        self.size += 1

        q = self.head

        for i in range(int((self.size-1)/2)): q = q.next
        self.middle = q

        return True
    
    def median(self):
        s = self.size
        if s % 2 == 0: m = (self.middle.data+self.middle.next.data)/2
        else: m = self.middle.data
        return m

class Stack(LinearList):
    
    def __init__(self):
        LinearList.__init__(self)

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

class Queue:

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

    def levelOrder(self):
        node = self.root
        
        q = Queue()
        
        while node is not None:
            print(node.info,end=" ")
            if node.left is not None: q.queue(node.left)
            if node.right is not None: q.queue(node.right)
                
            node = q.dequeue()
    
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
        #super().levelOrder()
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
        t.height = max(super().height(t.left),super().height(t.right)) + 1
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
            while self.contains(k,self.root) and k > -1:
                k -= 1
            return k

class BinaryDataHeap:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.heap = [float('-inf')]+[float('-inf')]*capacity
        self.data = [float('-inf')]+[float('-inf')]*capacity
        #self.heap = [None]*capacity

    def insert(self,key,data):
        if self.size == self.capacity:
            self.heap = self.heap + [float('-inf')]*self.capacity
            self.data = self.data + [float('-inf')]*self.capacity
            self.capacity *= 2
        #sift up
        sp = self.size + 1
        while key < self.heap[int(sp/2)]:
            self.heap[sp] = self.heap[int(sp/2)]
            self.data[sp] = self.data[int(sp/2)]
            sp = int(sp/2)
        self.heap[sp] = key
        self.data[sp] = data
        self.size +=1
        return True

    def findMin(self):
        if self.size > 0: return [self.heap[1],self.data[1]]
        
    def deleteMin(self):
        if self.size < 1: return None

        m = self.findMin()

        self.heap[1] = self.heap[self.size]
        self.data[1] = self.data[self.size]
        self.heap[self.size] = 0
        self.data[self.size] = 0
        self.size -= 1

        #sift down
        hole = 1
        tmp = self.heap[hole]
        tmp2 = self.data[hole]

        while hole*2 <= self.size:
            child = hole*2
            if hole*2+1 <= self.size and self.heap[child] > self.heap[child+1]:
                child +=1
            if self.heap[child] < tmp:
                self.heap[hole] = self.heap[child]
                self.data[hole] = self.data[child]
            else: break

            hole = child

        self.heap[hole] = tmp
        self.data[hole] = tmp2

        return m

class BinaryHeap:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.heap = [0]*capacity
        #self.heap = [None]*capacity

    def insert(self,x):
        if self.size == self.capacity-1:
            self.heap = self.heap + [0]*self.capacity
            self.capacity*=2
        #sift up
        sp = self.size + 1
        while x < self.heap[int(sp/2)]:
            self.heap[sp] = self.heap[int(sp/2)]
            sp = int(sp/2)
        self.heap[sp] = x
        self.size +=1
        return True

    def delete(self,x):
        if self.size > 0:
            for i in range(self.size):
                if(self.heap[i+1] == x):
                    sp = i+1
                    break

            while sp > 1:
                self.heap[sp] = self.heap[int(sp/2)]
                sp = int(sp/2)
            
            return self.deleteMin()

    def findMin(self):
        if self.size > 0: return self.heap[1]
        
    def deleteMin(self):
        if self.size < 1: return None

        m = self.findMin()

        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size -= 1

        #sift down
        hole = 1
        tmp = self.heap[hole]

        while hole*2 <= self.size:
            child = hole*2
            if hole*2+1 <= self.size and self.heap[child] > self.heap[child+1]:
                child +=1
            if self.heap[child] < tmp: self.heap[hole] = self.heap[child]
            else: break

            hole = child

        self.heap[hole] = tmp

        return m

    def heapSort(self):
        s = self.size
        arr = []

        for i in range(self.size):
            arr.append(self.deleteMin())
        
        if s % 2 == 0: m = (arr[int(s/2)]+arr[int(s/2)-1])/2
        else: m = arr[int(s/2)]

        return m

class HashNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self,card):
        self.size = 0
        self.m = card
        self.map = [None]*self.m
        self.ps = [1645333507,2971215073,1073807359,2147483647,2521008887,1442968193,1500450271]
        self.p = random.choice(self.ps)
        self.a = random.randint(1,self.p-1)
        self.b = random.randint(0,self.p-1)

    def get(self,key):
        index = self.getHash(key)
        n = self.map[index]
        if n is None: return
        while n and n.key != key:
            n = n.next
        if n is not None: return n.value

    def getHash(self,key):
        return ((self.a*key+self.b)%self.p)%self.m

    def add(self,key,value):
        m = HashNode(key,value)
        index = self.getHash(key)
        n = self.map[index]

        if n is None:
            self.map[index] = m
            self.size += 1
        elif n.key == key:
            n.value = value
            self.size += 1
        else:
            while n.next is not None:
                if n.key == key:
                    n.value = value
                    return
                n = n.next
            n.next = m
            self.size+=1
        
        self.reHash()
    
    def delete(self,key):
        index = self.getHash(key)
        if self.map[index] is None: return
        n = self.map[index]
        if n.key == key:
            self.map[index] = n.next
            self.size-=1
        while n.next and n.next.key != key:
            n = n.next
        if n.next is not None and n.next.key == key:
            n.next = n.next.next
            self.size-=1
        
    def reHash(self):
        if self.size/self.m > 0.9:
            self.p = random.choice(self.ps)
            self.a = random.randint(1,self.p-1)
            self.b = random.randint(0,self.p-1)
            newMap = self.map
            self.map = [None]*(2*self.m)
            self.size = 0
            self.m*=2
            for o in newMap:
                while o:
                    self.add(o.key,o.value)
                    self.size+=1
                    o = o.next

class StringHashMap:
    def __init__(self,card,lenght):
        self.size = 0
        self.m = card
        self.L = lenght
        self.map = [None]*self.m
        self.ps = [1645333507,2971215073,1073807359,2147483647,2521008887,1442968193,1500450271]
        self.p = random.choice(self.ps)
        self.x = random.randint(11,40)

    def get(self,key):
        index = self.getHash(key)
        if self.map[index] is None: return None
        n = self.map[index]
        while n and n.key != key:
            n = n.next
        if n is not None: return n.value

    def getHash(self,key):
        h = 0
        for i in reversed(key): 
            h = (h*self.x + ord(i))%self.p
        return h%self.m

    def add(self,key,value):
        m = HashNode(key,value)
        index = self.getHash(key)
        n = self.map[index]
        if n is None:
            self.map[index] = m
            self.size += 1
        elif n.key == key:
            n.value = value
            self.size += 1
        else:
            while n.next:
                if n.key == key:
                    n.value = value
                    return
                n = n.next
            n.next = m
            self.size+=1
        
        self.reHash()
    
    def delete(self,key):
        index = self.getHash(key)
        if self.map[index] is None: return
        n = self.map[index]
        if n.key == key:
            self.map[index] = n.next
            self.size-=1
        while n.next and n.next.key != key:
            n = n.next
        if n.key == key:
            n = n.next
            self.size-=1
        
    def reHash(self):
        if self.size/self.m > 0.9:
            self.p = random.choice(self.ps)
            self.x = random.randint(11,40)
            newMap = self.map
            self.map = [None]*(2*self.m)
            self.size = 0
            self.m*=2
            for o in newMap:
                while o:
                    self.add(o.key,o.value)
                    self.size+=1
                    o = o.next

if __name__ == "__main__":
    import string
    '''
    for i in range(900000): usuarios.add(str(i)+''.join(random.choice(string.ascii_lowercase) for _ in range(6)),random.randint(1000100100, 9999899899))
    c = 0
    for i in usuarios.map:
        if i is not None:
            c+=1
    print(usuarios.size/usuarios.m, len(usuarios.map), usuarios.size, usuarios.m, c)      
    '''
    