# 2015-08-18  Runtime: 216 ms
class LRUCache:
    # dictionary + doubly linked list, see the picture in http://www.programcreek.com/2013/03/leetcode-lru-cache-java/
    class Node:
        def __init__(self, key, val):
            self.key, self.val = key, val
            self.prev, self.next = None, None

    # @param capacity, an integer
    def __init__(self, capacity):
        self._capacity, self._size, self._d = capacity, 0, {}
        self._head, self._tail = self.Node(0, 0), self.Node(0, 0)
        self._head.next, self._tail.prev = self._tail, self._head

    # @return an integer
    def get(self, key):
        if key not in self._d:
            return -1
        self._insertNodeAtFirst(self._unlinkNode(self._d[key]))
        return self._d[key].val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, val):
        if key in self._d:
            self._insertNodeAtFirst(self._unlinkNode(self._d[key]))
            self._d[key].val = val
        else:
            if self._size == self._capacity:
                del self._d[self._tail.prev.key]
                self._unlinkNode(self._tail.prev)
            else:
                self._size += 1
            self._d[key] = self.Node(key, val)
            self._insertNodeAtFirst(self._d[key])
            
    def _unlinkNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node

    def _insertNodeAtFirst(self, node):
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node