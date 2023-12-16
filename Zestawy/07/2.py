# 2. Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

class Node:
    def __init__(self, val = None, index = None, next = None):
        self.val = val
        self.index = index
        self.next = next


def print_list(head):
    print('GUARDIAN -> ', end = '')
    while head.next != None:
        print(str(head.next.index) + ' : ' + str(head.next.val) + ' -> ', end='')
        head = head.next
    print('KONIEC')

def init():
    return Node()

def get(p, index):
    while p.next != None:
        if p.next.index == index:
            return p.next.val
        elif p.next.index > index:
            break
        p = p.next
    return 0

def add(p, index, value):
    start = p
    while p.next != None and p.next.index < index:
        p = p.next
    
    if p.next != None and p.next.index == index:
        p.next.val = value
    else:
        new_node = Node(value, index, p.next)
        p.next = new_node
    return start


g = init()
g = add(g, 4, 4)
print_list(g)
g = add(g, 2, 3)
print_list(g)
g = add(g, 4, 5)
print_list(g)
g = add(g, 100, 100)
print_list(g)