class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    new_node = Node(data)

    if not head:
        return new_node

    if data <= head.data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head

def print_list(head):
    """Helper function to print the linked list."""
    elements = []
    while head:
        elements.append(head.data)
        head = head.next
    print(" -> ".join(map(str, elements)) + " -> None")

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    head = sorted_insert(head, 4)
    print_list(head)  
    head = Node(1)
    head.next = Node(7)
    head.next.next = Node(8)
    head = sorted_insert(head, 5)
    print_list(head)

    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(9)
    head = sorted_insert(head, 7)
    print_list(head)
