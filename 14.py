class CircularDeque:
    def __init__(self, capacity):
        if capacity <= 0:
            print("ظرفیت باید عدد مثبت باشد")
        self.capacity = capacity
        self.deque = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity
    def append(self, item):
        if self.is_full():
            print("صف پر است - نمی‌توان از عقب اضافه کرد")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.deque[self.rear] = item
        self.size += 1
    def appendleft(self, item):
        if self.is_full():
            print("صف پر است - نمی‌توان از جلو اضافه کرد")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity
        self.deque[self.front] = item
        self.size += 1
    def popleft(self):
        if self.is_empty():
            print("صف خالی است - نمی‌توان از جلو حذف کرد")
        item = self.deque[self.front]
        self.deque[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    def pop(self):
        if self.is_empty():
            print("صف خالی است - نمی‌توان از عقب حذف کرد")
        item = self.deque[self.rear]
        self.deque[self.rear] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return item
    def peek_front(self):
        if self.is_empty():
            print("صف خالی است")
        return self.deque[self.front]
    def peek_rear(self):
        if self.is_empty():
            print("صف خالی است")
        return self.deque[self.rear]
    def __len__(self):
        return self.size
    def display(self):
        if self.is_empty():
            print("صف دوطرفه خالی است")
            return
        print("محتویات صف دوطرفه:", end=" ")
        i = self.front
        while True:
            print(self.deque[i], end=" ↔ ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print("(پایان)")
