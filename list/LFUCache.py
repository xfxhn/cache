from list.doubleLinkedList import Node, DoubleLinkedList


# LFU最不经常使用算法，记录每次调用的次数，把使用频率最短的淘汰掉

class LFUNode(Node):
    def __init__(self, key, value):
        super().__init__(key, value)
        # 记录频率
        self.frequency = 0


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        # key值记录频率，value值记录频率对应的双向链表
        self.freq_map = {}

    # 更新节点频率的操作
    def __update(self, node):
        # 把频率取出
        freq = node.frequency
        # 把从频率映射节点取出删掉
        node = self.freq_map[freq].remove(node)

        # 删除频率映射里链表为0的映射
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]

        # 这个频率是永远累加的
        freq += 1
        # 把频率赋值给节点
        node.frequency = freq

        # 频率没在频率映射里就创建一个映射
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinkedList()

        # 把节点放在频率对应的链表里
        self.freq_map[freq].push(node)

    def get(self, key):
        if key in self.map:
            node = self.map.get(key)
            # 更新节点的频率
            self.__update(node)
            print(node, 'asd')
            return node.value

    def put(self, key, value):

        # if self.capacity == 0:
        #     return
        # #
        if key in self.map:
            node = self.map.get(key)
            # 重新赋值
            node.value = value
            # 更新频率节点
            self.__update(node)
        else:
            if self.size == self.capacity:
                # 获取最低频率
                min_freq = min(self.freq_map)
                print(self.freq_map)
                print(min_freq, '最低')

                # 把频率最低的链表末尾淘汰掉
                node = self.freq_map[min_freq].pop()

                # 删掉相关的映射
                del self.map[node.key]
                self.size -= 1
            # 创建个节点
            node = LFUNode(key, value)
            # 把频率设置成1，因为这样已经调用了一次
            node.frequency = 1
            self.map[key] = node
            # 判断频率在不在频率映射里，不在就创建一个
            if node.frequency not in self.freq_map:
                self.freq_map[node.frequency] = DoubleLinkedList()

            # 把节点放进频率映射的链表里
            self.freq_map[node.frequency].push(node)
            self.size += 1

    def __repr__(self):
        for k, v in self.freq_map.items():
            print('**************************')
            print('频率%d' % k)
            print(self.freq_map[k])
            print('**************************')
        print(self.freq_map)
        return str(self.map)


if __name__ == '__main__':
    lfu = LFUCache(2)
    lfu.put('我', 1)
    lfu.put('是', 2)
    lfu.put('是', 2)
    lfu.put('帅', 2)
    lfu.put('帅', 2)
    lfu.put('帅', 2)
    lfu.put('哥', 2)
    lfu.put('哥', 2)
    lfu.put('哥', 2)
    lfu.put('哥', 2)
    lfu.put('帅', 2)
    lfu.put('我', 1)
    # lfu.put(9, 2)
    print(lfu)
