# 2016-03-28  17 tests, 204 ms
class LRUCache(object):

    class ListNode(object):
        def __init__(self, k, v):
            self.k, self.v = k, v
            self.prev, self.next = None, None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity, self.size, self.d = capacity, 0, {}
        self.head, self.tail = self.ListNode(0, 0), self.ListNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def __unlink_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def __insert_at_head(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.d:
            return -1
        node = self.d[key]
        self.__unlink_node(node)
        self.__insert_at_head(node)
        return node.v

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.d:  # hit
            node = self.d[key]
            node.v = value
            self.__unlink_node(node)
            self.__insert_at_head(node)
        else:  # insert
            if self.size == self.capacity:
                least_recently_used_node = self.tail.prev
                self.__unlink_node(least_recently_used_node)
                del self.d[least_recently_used_node.k]
                self.size -= 1
            new_node = self.ListNode(key, value)
            self.__insert_at_head(new_node)
            self.d[key] = new_node
            self.size += 1
