#class stak
def __init__(self, limit):
    self.st=[]
    self.lim=limit
def push (self, x):
    if len(self.st)>=self.lim-1:
        print("stak is full!")
    return-1
    self.st.append(x)
def pop(self):
    if len (self.st)==0:
        print("stak is empty!")
        return-1
    return self.st
def peek (self):
    if len (self.st)==0:
        print("stak is empty!")
        return-1
    return self.st[-1]
def show (self):
    print (stak.st)
def display (self):
    for i in reverse (self.st):
        print(i)
def find (self, f):
    found=False
    for i in range (len (self.st)):
        if self.st[i]==f:
            print ("i")
        found=True
    if not found:
        print("not found!")
def replace (self, f, x):
    for i in range (len (self.st)):
        if self.st[i]==f:
            self.st[i]=x
def replace1 (self, f, x):
    for i in range (len(self.st)-1, -1, -1):
        if self.st[i]==f:
            self.st[i]=x
            return