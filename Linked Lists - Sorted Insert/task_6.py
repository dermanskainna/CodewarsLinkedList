'''
sorted insert
'''
class Node(object):
    '''
    node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    '''
    sorted insert
    '''
    curr = head
    n_1 = Node(data)
    if head is None or data < head.data:
        n_1.next = head
        return n_1

    while curr.next is not None and curr.next.data < data:
        curr = curr.next

    n_1.next = curr.next
    curr.next = n_1
    return head
