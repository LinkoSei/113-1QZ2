class Stack:
    def __init__(self, size):
        self.stack = [None] * size  # 初始化固定大小的陣列
        self.size = size
        self.top = -1  # 堆疊頂端指標，初始化為 -1 表示空堆疊

    def Push(self, item):
        if self.IsFull():
            print("堆疊已滿，無法Push新元素")
            return
        self.top += 1
        self.stack[self.top] = item

    def Pop(self):
        if self.IsEmpty():
            print("堆疊為空，無法Pop(out)元素")
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def TopItem(self):
        if self.IsEmpty():
            print("堆疊為空，沒有頂端元素")
            return None
        return self.stack[self.top]

    def IsEmpty(self):
        return self.top == -1

    def IsFull(self):
        return self.top == self.size - 1

    def __str__(self):
        return str(self.stack[:self.top + 1])

# 示例操作
stack = Stack(5)
print("是否為空堆疊:", stack.IsEmpty())  # True
stack.Push(10)
stack.Push(20)
stack.Push(30)
print("堆疊內容:", stack)
print("堆疊頂端元素:", stack.TopItem())  # 30
stack.Pop()
print("堆疊內容:", stack)
print("是否為滿堆疊:", stack.IsFull())  # False
stack.Push(40)
stack.Push(50)
stack.Push(60)
print("是否為滿堆疊:", stack.IsFull())  # True
print("堆疊內容:", stack)
