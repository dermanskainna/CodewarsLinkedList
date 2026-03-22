'''
Swap
'''
class Node:
    '''
    node
    '''
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    '''
    swap
    '''
    if not head or not head.next:
        return head

    new_head = head.next

    current = head
    prev = None

    while current and current.next:
        first = current
        second = current.next

        first.next = second.next
        second.next = first

        if prev:
            prev.next = second

        prev = first
        current = first.next

    return new_head
