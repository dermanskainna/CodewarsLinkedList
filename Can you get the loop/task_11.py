'''
loop
'''
class Node(object):
    '''
    node
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None


def loop_size(node):
    '''
    loop
    '''
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    count = 1
    current = slow.next

    while current != slow:
        current = current.next
        count += 1

    return count
