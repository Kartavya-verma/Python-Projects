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


firstNode = Node("kv")

linkedlist = LinkedList()

linkedlist.insertend(firstNode)

secondnode = Node("kv1")
linkedlist.insertend(secondnode)

thirdnode = Node("kv2")
linkedlist.inserthead(thirdnode)

linkedlist.printlist()
