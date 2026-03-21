'''
task 3
'''
class Node:
    '''
    Node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    '''
    new head
    '''
    new = Node(data)
    if head:
        new.next = head
    return new

def build_one_two_three():
    '''
    1 -> 2 -> 3 -> None
    '''
    n3 = Node(3)
    n2 = Node(2)
    n2.next = n3
    head = Node(1)
    head.next = n2
    return head
