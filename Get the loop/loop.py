class Node:
    def __init__(self):
        self.next = None


def loop_size(node):
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0

    loop_length = 1
    current = slow.next
    while current != slow:
        loop_length += 1
        current = current.next

    return loop_length


if __name__ == "__main__":
    def fixed_tests():
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        assert loop_size(node1) == 3, "Should return loop size of 3"

        nodes = [Node() for _ in range(50)]
        for i in range(49):
            nodes[i].next = nodes[i + 1]
        nodes[49].next = nodes[21]
        assert loop_size(nodes[0]) == 29, "Should return loop size of 29"

        print("All tests passed!")


    fixed_tests()