from list.doubleLinkedList import Node, DoubleLinkedList


# LRU最进最少使用算法
# 淘汰末尾，最近使用的放在最前面
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if key in self.map:
            # 把节点拿出来
            node = self.map.get(key)
            self.list.remove(node)
            self.list.unshift(node)
            return node.value

    def put(self, key, value):
        if key in self.map:
            node = self.map.get(key)
            # 先删除这个节点
            self.list.remove(node)
            # 更新value值
            node.value = value
            # 把节点放在最前面确保是最新调用的
            self.list.unshift(node)
        else:
            # 创建新的节点
            node = Node(key, value)
            # 先判断容量超过没
            if self.size >= self.capacity:
                # 把最后一个节点删除
                old_node = self.list.pop()
                # 把原来的映射关系删除
                del self.map[old_node.key]

            self.list.unshift(node)
            self.map[key] = node
            self.size += 1

    def __repr__(self):
        return str(self.list)


if __name__ == '__main__':
    lru = LRUCache(3)

    lru.put(1, 2)
    lru.put(2, 3)
    lru.put(3, 4)
    lru.get(1)
    lru.put(4, 5)
    lru.get(3)
    print(lru.get(9))

    print(lru, 'xiaofeng')
