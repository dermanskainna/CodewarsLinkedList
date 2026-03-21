'''
move head
'''
class Node(object):
    '''
    head
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    '''
    context
    '''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''
    move head
    '''
    if source is None:
        raise ValueError("Source list is empty")

    first_node = source
    source = source.next
    first_node.next = dest
    dest = first_node

    return Context(source, dest)
