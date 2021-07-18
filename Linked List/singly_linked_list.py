class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newnode):

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

linkedlist.insert(firstNode)

secondnode = Node("kv1")
linkedlist.insert(secondnode)

thirdnode = Node("kv2")
linkedlist.insert(thirdnode)

linkedlist.printlist()
