import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head:
            _sorted = ListNode(head.val)
            head = head.next
            while head:
                v = head.val
                x = _sorted
                p = None
                while x and x.val < v:
                    p = x
                    x = x.next

                node = ListNode(head.val)
                if p is None:
                    node.next = _sorted
                    _sorted = node
                else:
                    p.next = node
                    node.next = x

                head = head.next
            return _sorted

def build_list(lst):
    nodes = [ListNode(el) for el in lst]
    for x, y in zip(nodes[:-1], nodes[1:]):
        x.next = y
    return nodes[0] if nodes else None
    
def print_list(x):
    while x:
        print(x.val, end=" ")
        x = x.next
    print()

def to_list(x):
    lst = list()
    while x:
        lst.append(x.val)
        x = x.next
    return lst

if __name__ == "__main__":
    solution = Solution()
    for i in range(1000):
        n = random.randint(0, 100)
        values = [random.randint(1, 10) for x in range(n)]
        x = build_list(values)
        _sorted = solution.insertionSortList(x)
        sorted_values = to_list(_sorted)
        values.sort()
        assert values == sorted_values

