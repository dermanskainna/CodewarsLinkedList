'''
get nth node
'''
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
       self.data = data
       self.next = next

def get_nth(node, index):
    '''
    node №index
    '''
    if node is None or index < 0:
        raise IndexError("Invalid index")
    curr = node
    for _ in range(index):
        if curr is None:
            raise IndexError("Index out of bounds")
        curr = curr.next
    if curr is None:
        raise IndexError("Index out of bounds")
    return curr
