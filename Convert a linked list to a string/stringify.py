class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    result = []
    while node is not None:
        result.append(str(node.data))
        node = node.next
    result.append("None")
    return " -> ".join(result)
