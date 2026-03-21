'''
str -> ll
'''
class Node:
    '''
    Node
    '''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    '''
    str -> ll
    '''
    if list_repr == "None":
        return None

    parts = list_repr.split(" -> ")
    head = Node(int(parts[0]))
    current = head

    for value in parts[1:-1]:
        new_node = Node(int(value))
        current.next = new_node
        current = new_node
    return head
