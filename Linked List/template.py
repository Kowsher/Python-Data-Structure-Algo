# Definition for singly-linked list.
class Node:
     def __init__(self, val=None, next=None):
         self.val = val
         self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        a =Node(data)   
        a.next = self.head 
        self.head = a

linklist = LinkedList()
linklist.add(1)
linklist.add(2)
linklist.add(3)

while(head != None):
    print(head.val)
    head = head.next
