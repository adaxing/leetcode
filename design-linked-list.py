class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self, val, next=None):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.next = next

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < len(self.val):
            return self.val[index]
        else:
            return -1
    
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.val.insert(0,val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.val.insert(len(self.val), val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < len(self.val):
            self.val.insert(index, val)
        elif index == len(self.val):
            self.addAtTail(val)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < len(self.val):
            self.val.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList([1,2,4])
param_1 = obj.get(2)
obj.addAtHead(5)
obj.addAtTail(8)
obj.addAtIndex(6,7)
obj.deleteAtIndex(4)
print(obj.val)

