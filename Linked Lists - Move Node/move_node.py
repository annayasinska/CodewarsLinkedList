class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError("Source list is empty")

    new_source = source.next
    source.next = dest
    dest = source

    return Context(new_source, dest)

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def build_one_two_three():
    return push(push(push(None, 3), 2), 1)


def print_list(head):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    return " -> ".join(result) + " -> None"

if __name__ == "__main__":
    source = build_one_two_three()
    dest = push(push(push(None, 6), 5), 4)

    result = move_node(source, dest)

    print("Updated Source:", print_list(result.source))
    print("Updated Dest:", print_list(result.dest))