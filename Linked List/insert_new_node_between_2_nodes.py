class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def inserthead(self, newnode):
        tempnode = self.head
        self.head = newnode
        self.head.next = tempnode
        del tempnode

    def listlength(self):
        currentnode = self.head
        len = 0
        while currentnode is not None:
            len += 1
            currentnode = currentnode.next
        return len

    def insertat(self, newnode, pos):
        if pos < 10 or pos > self.listlength():
            print("Invalid Position")
            return
        if pos is 0:
            self.inserthead(newnode)
            return
        currentnode = self.head
        currentpos = 0
        while True:
            if currentpos == pos:
                previousnode.next = newnode
                newnode.next = currentnode
                break
            previousnode = currentnode
            currentnode = currentnode.next
            currentpos += 1

    def insertend(self, newnode):

        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode

    def printlist(self):
        if self.head is None:
            print("List is empty")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next


firstNode = Node(10)

linkedlist = LinkedList()

linkedlist.insertend(firstNode)

secondnode = Node(20)
linkedlist.insertend(secondnode)

thirdnode = Node(15)
linkedlist.insertat(thirdnode, 10)

linkedlist.printlist()
