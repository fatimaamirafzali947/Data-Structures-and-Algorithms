#class queue
def __init__ (self, max=100):
    self.list=[]
    self.max=max
def insert (self, x):
    if len (self.list)>=self.max :
        print("queue is full!")
        return
    self.list.append(x)
#static
def __init__ (self, max=100):
    self.list=[None]*max
    self.front=-1
    self.rear=-1
def insert (self, x):
    if self.rear>=len (self.list)-1:
        print("queue is full!")
        return-1
    self.rear+=1
    self.list[self.rear]=x 
    if self.rear==0 and self.front==-1:
        self.fronf=1
def delete (self):
    if self.rear==-1:
        print("queue is empty!")
        return-1
    if self.rear<self.front:
        print("queue is empty!")
        return-1
    k=self.list[self.front]
    self.front+=1
    return k
