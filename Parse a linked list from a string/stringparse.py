class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
def linked_list_from_string(s):
    if s.strip() in {"null", "None"}:
        return None
    values = s.split(" -> ")
    head = None
    current = None
    for e in values:
        if e in {"null", "None"}:
            break
        node = Node(int(e))
        if not head:
            head = node
        else:
            current.next = node
            