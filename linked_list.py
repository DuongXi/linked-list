class Node:
#khởi tạo một phần tử(nút) mới
    
    def __init__(self, data):
       self.data = data
       self.next = None

class linkedList:
#linked list ở đây sẽ chỉ là single linked list    

    def __init__(self):
        #khởi tạo linked list
        self.size = 0
        self.head = None

    def length(self):
        #trả về độ dài linked list
        return self.size
    
    def isEmpty(self):
        #kiểm tra linked list có rỗng không
        return self.size == 0
    
    def printList(self):
        #in ra linked list
        curNode = self.head
        if self.size >= 1:
            print(curNode.data, end=" ")
            while(curNode.next != None):
                curNode = curNode.next
                print(curNode.data, end=" ")
            print()
        else:
            print("The list is currently empty")
    
    def appendList(self,val):
        #thêm một phần tử vào cuối linked list
        newNode = Node(val)
        curNode = self.head
        if self.size == 0:
            self.head = newNode
        elif self.size == 1:
            self.head.next = newNode
        else:
            while(curNode.next != None):
                curNode = curNode.next
            curNode.next = newNode
        self.size += 1
    
    def removeTail(self):
        #loại đi phần tử cuối linked list
        curNode = self.head
        if self.size == 0:
            print("The list is currently empty")
        else:
            if(self.head.next == None):
                self.head = None
            else:
                while(curNode.next.next != None):
                    curNode = curNode.next
                curNode.next = None
            self.size -= 1
    
    def addFirst(self, val):
        #thêm một phần tử vào đầu linked list
        newNode = Node(val)
        if self.size == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1
        
    def removeHead(self):
        #loại bỏ một phần tử ở đầu linked list
        if self.size == 0:
            print("The list is currently empty")
        else:
            self.head = self.head.next
            self.size -= 1
            
    def insert(self, val, index):
        #thêm một phần tử vào vị trí bất kì của linked list
        if index > self.size:
            print("Index out of range")
        else:
            if index == 1:
                self.addFirst(val)
            else:
                count = 1
                newNode = Node(val)
                curNode = self.head
                while(count != index-1):
                    curNode = curNode.next
                    count += 1
                newNode.next = curNode.next
                curNode.next = newNode
                self.size += 1
    
    def remove(self,index):
        #xoá một phần tử ở vị trí bất kì của linked list
        count = 1
        curNode = self.head
        if self.size == 0:
            print("The list is currently empty")
        else:
            if index > self.size:
                print("Index out of range")
            else:
                if index == 1:
                    self.removeHead()
                else:
                    while(count != index-1):
                        curNode = curNode.next
                        count += 1
                    curNode.next = curNode.next.next
                    self.size -= 1
#Vẫn có thể còn nhiều phương thức chưa được cho vào nhưng đây là một số cái tôi hiện tại nghĩ ra được
