
# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    current = node
    position = 0

    while current is not None:
        if position == index:
            return current
        current = current.next
        position += 1

    raise Exception("Index out of range or the list is empty.")

if __name__ == "__main__":
    head = Node(42, Node(13, Node(666)))

    print(get_nth(head, 1).data)

    print(get_nth(head, 0).data)
    print(get_nth(head, 2).data)  
    try:
        print(get_nth(head, 3).data)
    except Exception as e:
        print(e)