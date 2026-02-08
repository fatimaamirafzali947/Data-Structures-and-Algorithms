#class linked_list()
def __init__ (self):
    self.head=None 
def insert (self, x):
    if self.head==None:
        a=node(x)
        self.head=a
        return
def insert_last(self, x):
    if self.head is None:
        self.head=node(x)
    else:
        a=node(x)
        c=self.head
        while c.next:
            c=c.next
        c.next=a 
def insert_first (self, x):
    if self.head is None:
        self.head=node(x)
    else:
        a=node(x)
        a.next=self.head
        self.head=a
def insert_after (self, x, y):
    if x is None or y is None:
        print("cant be none!")
    if self.head is None:
        print("list is empty!")
        return
    c=self.head
    while c:
        if c.data==x:
            a=node(y)
            a.next=c.next 
            c.next=a 
            return
        c=c.next 
    print("x not found!")
def insert_befor (self, x, y):
    if self.head==None:
        print("list is empty!")
        return
    if self.head.data==x:
        self.insert.first(y)
    c=self.head
    while c.next:
        if c.next.data==x:
            a=node(y)
            a.next=c.next 
            c.next=a 
            return
        c=c.next 
    print("not found!")
def del_first (self):
    if self.head:
        c=self.head
        self.head=self.head.next 
        del c 
    else:
        print("list is empty!")
def del_last (self):
    if self.head is None:
        print ("list is empty!")
        return
    if self.head.next==None:
        del self.head
        self.head=None
        return
    c=self.head
    while c.next.next:
        c=c.next 
    a=c.next 
    c.next=None
    del a
def del_first (self):
    if self.head is None:
        print("list is empty!")
    else:
        c=self.head
        self.head=self.head.next 
        del c
def del_last (self):
    if self.head is None:
        print("list is empty!")
    if self.head is None:
        self.del_first()
    else:
        c=self.head
        while c.next.next:
            c=c.next 
        a=c.next 
        c.next=None
        del a
def del_after (self, x):
    if self.head is None:
        print("list is empty!")
        return
    c=self.head
    while c:
        if c.data==x:
            if c.next:
                a=c.next 
                c.next=c.next.next 
                del a
                return
            print("error!!!")
        c=c.next 
    print("x not found!")
def del_before (self, x):
    if self.head is None:
        print("list is empty!")
        return
    if self.head.data==x:
        print("before x is not node!")
        return
    if self.head.next is None:
        print("error!!!")
        return
    if self.next.data==x:
        self.del_first()
        return
    if self.head.next is None:
        print("error2!!!")
        return
    c=self.head
    while c.next.next:
        if c.next.next.data==x:
            a=c.next 
            c.next=c.next.next 
            del a
            return
        c=c.next 
    print ("x not found!")
