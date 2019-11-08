from list.doubleLinkedList import Node, DoubleLinkedList


# 先进先出算法

class FIFOCache:
    def __init__(self, capacity):
        # 容量
        self.capacity = capacity
        # 记录长度
        self.size = 0
        # 记录映射关系
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if key in self.map:
            node = self.map.get(key)
            return node.value

    def put(self, key, value):
        if not self.capacity:
            return

        if key in self.map:
            # 先把节点取出来
            node = self.map.get(key)
            # 删除节点列表里的节点
            self.list.remove(node)
            # 设置新值
            node.value = value
            # 重新添加到列表里
            self.list.push(node)
        else:
            # 先判断缓存是不是满了
            if self.size >= self.capacity:
                # 把列表最前面那个删除掉
                node = self.list.shift()
                del self.map[node.key]
                self.size -= 1

            # 往列表最后添加一个节点
            node = Node(key, value)
            self.list.push(node)
            # 保存映射关系
            self.map[key] = node
            self.size += 1

    def __repr__(self):
        return str(self.list)


if __name__ == 'main':
    cache = FIFOCache(2)
    cache.put(4, 5)
    cache.put(2, 6)
    cache.put(1, 5)
    print(cache.get(1))
    # cache.put(4, 5)
    # cache.put(7, 8)
    print(cache)
