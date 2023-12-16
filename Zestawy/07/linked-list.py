
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(str(head.val) + ' -> ', end='')
        head = head.next
    print('KONIEC')

def remove_element(p, to_delete):
    prev = None
    start = p

    while p != None:
        if p.val == to_delete:
            if prev == None:
                return p.next
            else:
                prev.next = prev.next.next
                return start
        prev = p
        p = p.next
    
    return start

def add_element(p, to_add):
    start = p
    prev = None
    while p != None:
        prev = p
        p = p.next
    
    if prev == None:
        return Node(to_add)
    prev.next = Node(to_add)
    return start

c = Node(3)
b = Node(2, c)
a = Node(1, b)
g = Node(None, a)

print_list(a)
a = add_element(a, 4)
print_list(a)

# prev = 1
# 
# 1 -> 2 -> 3
