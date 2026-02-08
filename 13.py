class CircularQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            print("ظرفیت باید عدد مثبت باشد")
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity
    def enqueue(self, item):
        if self.is_full():
            print("صف پر است - نمی‌توان اضافه کرد")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print("عنصر {item} اضافه شد")
    def dequeue(self):
        if self.is_empty():
            print("صف خالی است - نمی‌توان حذف کرد")
        item = self.queue[self.front]
        self.queue[self.front] = None 
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    def peek(self):
        if self.is_empty():
            print("صف خالی است - نمی‌توان دید")
        return self.queue[self.front]
    def __len__(self):
        return self.size
    def display(self):
        if self.is_empty():
            print("صف خالی است")
            return
        print("محتویات صف:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" → ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print("(پایان)")
