from functools import reduce

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        iter1 = IterListNodes(self)
        iter2 = IterListNodes(other)
        for x, y in zip(iter1, iter2):
            if x!=y:
                return False
        return True

    def __len__(self):
        iter = IterListNodes(self)
        sum=0
        for i in iter:
            sum += 1
        return sum


    def __str__(self):
        iter1 = IterListNodes(self)
        l = list(iter1)
        l.reverse()
        return reduce(lambda x,y: x + "" + y, map(str, l))

class IterListNodes():
    def __init__(self, ln):
        self.list_node = ln
        self.current = ln

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        retv = self.current.val
        self.current = self.current.next
        return retv



class Solution:
    @staticmethod
    def new_list_nodes(nodelist):
        nodes= {}
        for i,num in enumerate(nodelist):
            node = ListNode(num)
            nodes[i] = node
        for i in range (0, len(nodes)-1):
            nodes.get(i).next = nodes.get(i+1)
        return nodes.get(0)
    @staticmethod
    def two_sum_nums(node1, node2):
        ret = ListNode(0)
        parent = ret
        current = parent.next
        add_on = 0
        while (node1 is not None) or (node2 is not None):
            v1 = 0 if node1 is None else node1.val
            v2 = 0 if node2 is None else node2.val
            value = v1 + v2 + add_on
            if value >= 10:
                add_on = 1
                value -= 10
            else:
                add_on = 0
            current = ListNode(value)
            parent.next = current
            parent = current
            if(node1 is not None):
                node1 = node1.next
            if(node2 is not None):
                node2 = node2.next
        if add_on == 1:
            parent.next = ListNode(1)
        return ret.next