class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end='')
        head = head.next
    print('KONIEC')

def reverse(p):
    if p.next == None:
        return p, p
    rev_start, rev_end = reverse(p.next)
    p.next = None
    rev_end.next = p
    return rev_start, p

# 3 -> 2 -> 1
# reverse(Node(3)) -> 1, 2, 3

c = Node(3)
b = Node(2, c)
a = Node(1, b)

print_list(reverse(a)[0])