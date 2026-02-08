#class c-queue
def __init__ (self, max):
    self.list=[]*max
    self.front=-1
    self.resr=-1
def insert (self, x):
    if self.front==-1:
        self.list[0]=x 
        self.front=0
        self.rear=0
        return
    if (self.rear+1)%(len(self.list))==self.front:
        print("queue is full!")
        return
    rear=(rear+1)%(len(self.list))
    self.list[rear]=x 
def delete (self):
    if self.front==-1:
        print("queue is empty!")
        return
    if self.front==self.rear:
        k=self.list[self.front]
        self.front=-1
        self.rear=-1
        return k
    k=self.list[self.front]
    self.front=(self.front+1)%(len(self.list))
    return k
def isempty (self):
    return self.front==-1
def isfull (self):
    return (self.rear+1)% len(self.list)==self.front 
def show_valid (self):
    if self.rear >= self.front:
        for i in range (self.front, len(self.list+1)):
            print(self.list[i])
    else:
        for i in range (self.front, len(self.list),1 ):
            print(self.list[i])
        for i in range (self.rear+1):
            print(self.list[i])
def show_invalid (self):
    if self.rear>=self.front:
        for i in range (self.rear+1, len(self.list), 1):
            print(self.list[i])
        for i in range (self.front):
            print(self.list[i])
    else:
        for i in range ((self.rear+1), (self.front), 1):
            print(self.list[i])
def find (self, x):
    for i in range (len(self.list)):
        if self.list[i]==x:
            return i
        print("not found")
