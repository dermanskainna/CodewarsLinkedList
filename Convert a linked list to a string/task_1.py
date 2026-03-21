'Convert ll -> str'
class Node():
    '''
    Node
    '''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    '''
    ll -> str
    '''
    res = ''
    while node:
        res += f'{node.data} -> '
        node = node.next
    res += 'None'
    return res
