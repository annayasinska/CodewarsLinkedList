class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("Input list must have at least two nodes.")

    first_head = None
    second_head = None
    first_tail = None
    second_tail = None

    current = head
    is_first_list = True

    while current:
        if is_first_list:
            if first_head is None:
                first_head = current
                first_tail = current
            else:
                first_tail.next = current
                first_tail = first_tail.next
        else:
            if second_head is None:
                second_head = current
                second_tail = current
            else:
                second_tail.next = current
                second_tail = second_tail.next

        current = current.next
        is_first_list = not is_first_list

    if first_tail:
        first_tail.next = None
    if second_tail:
        second_tail.next = None

    return Context(first_head, second_head)


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    result = alternating_split(head)

    first = result.first
    while first:
        print(first.data, end=" -> ")
        first = first.next
    print("None")

    second = result.second
    while second:
        print(second.data, end=" -> ")
        second = second.next
    print("None")
