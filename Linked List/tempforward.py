# Definition for singly-linked list.
class Node:
     def __init__(self, val=None, next=None):
         self.val = val
         self.next = next
    

class LinkedList:
    def __init__(self):
        self.head1 = Node()
        self.head = self.head1

    def add(self,data):
        a =Node(data)   
         
        self.head.next = a
        a.next=None 
        self.head=a

    
      




