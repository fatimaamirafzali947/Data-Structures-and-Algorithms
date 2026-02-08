#class dnode
def __init__ (self, d):
    self.data=d
    self.next=None
    self.prev=None

#class dlinked list
def __init__ (self):
    self.head=None
def insert_first (self, x):
    if self.head is None:
        self.head=dnode(x)
    else:
        a=dnode(x)
        a.next=self.head
        a.next.prev=a
        self.head=a
def insert_last (self, x):
    if self.head is None:
        self.head=dnode(x)
    else:
        c=self.head
        while c.next:
            c=c.next 
            a=dnode(x)
            c.next=a
            a.prev=c
def insert_after (self, x, y):
    if self.head is None:
        print("error0")
        return
    c=self.head
    while c:
        if c.data==x:
            a=dnode(y)
            a.next=c.next 
        if c.next:
            c.next.prev=a
        c.next=a
        a.prev=c
        return
    c=c.next 
    print("not found!")
def insert_befor (self, x, y):
    if self.head is None:
        print("error 0!")
    if self.head.data==x:
        self.insert_first(y)
        return
    c=self.head
    while c:
        if c.data==x:
            a=dnode(y)
            a.next=c
            a.prev=c.prev
            c.prev.next=a
            c.prev=a
            return
        c=c.next 
        print("not found!")
def del_first (self):
    if self.head is None:
        print("error0!!!")
        return
    c=self.head
    self.head=c.next 
    del c
def del_last (self):
    if self.head is None:
        print("error0")
        return
    c=self.head
    while c.next:
        c=c.next 
    if c.prev:
        c.prev.next=None
    else:
        self.head=None
        del c
def del_after (self, x):
    if self.head is None:
        print("error0!!!")
        return
    c=self.head
    while c:
        if c.data==x:
            if c.next:
                a=c.next 
                c.next=c.next.next 
                if c.next:
                    c.next.prev=c
                del a
                return
            c=c.next 
        print("not found!")
def del_befor (self, x):
    if self.head is None:
        print("error0!")
        return
    if self.head.data==x:
        print("errorx1")
        return
    if self.head.next is None:
        print("error1")
        return
    c=self.head
    while c:
        if c.data==x:
            if c.prev:
                a=c.prev
                c.prev=a.prev
                if c.prev:
                    c.prev.next=c
                del a
            c=c.next 
        print("not found!")
def del_x (self, x):
    if self.head is None:
        print("error0!")
        return
    if self.head.data==x:
        self.del_first()
        return
    c=self.head
    while c:
        if c.data==x:
            c.prev.next=c.next 
            if c.next:
                c.next.prev=c.prev
            del c
            return
        c=c.next 
    print("not found!")
def del_all (self):
    while self.head:
        self.del_self()
