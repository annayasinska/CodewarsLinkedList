class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head):
    if not head or not head.next:
        return head

    rest = reverse(head.next)

    head.next.next = head
    head.next = None

    return rest

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    a = Node(2)
    b = Node(1)
    c = Node(3)
    d = Node(6)
    e = Node(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print("Original linked list:")
    print_list(a)

    reversed_head = reverse(a)

    print("\nReversed linked list:")
    print_list(reversed_head)
