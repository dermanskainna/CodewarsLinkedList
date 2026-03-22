'''
split
'''
class Node(object):
    '''
    node
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    '''
    for result
    '''
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    '''
    split
    '''
    if not head or not head.next:
        raise ValueError

    l1 = Node()
    l2 = Node()
    cur_1 = l1
    cur_2 = l2

    c = 1
    while head:
        temp = head.next

        if c % 2 == 1:
            cur_1.next = head
            cur_1 = cur_1.next
        else:
            cur_2.next = head
            cur_2 = cur_2.next

        head.next = None
        head = temp
        c += 1

    return Context(l1.next, l2.next)
