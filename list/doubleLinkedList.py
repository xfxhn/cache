# 定义节点
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # 上个节点的引用
        self.prev = None
        # 下个节点的引用
        self.next = None

    # 打印类的实例会调用这个方法
    def __repr__(self):
        return '{%s:%s}' % (self.key, self.value)


class DoubleLinkedList:
    def __init__(self, capacity=0xffffff):
        # 容量
        self.capacity = capacity
        # 头部指针
        self.head = None
        # 尾部指针
        self.tail = None
        # 记录存储了多少节点
        self.size = 0

    # 添加头部节点
    def __unshift(self, node):
        # 判断头部是不是空的
        if not self.head:
            self.head = node
            self.tail = node
            # 改变节点引用
            self.head.prev = None
            self.head.next = None
        else:
            # 改变当前节点的下个引用
            node.next = self.head
            # 当前头部节点的上个引用
            self.head.prev = node
            # 改变头部指针
            self.head = node
            # 改变头部节点的上个引用
            self.head.prev = None

        # 把链表的长度加1
        self.size += 1
        return node

    # 添加尾部节点
    def __push(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
            self.tail.prev = None
            self.tail.next = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
        self.size += 1
        return node

    # 删除任意节点
    def __remove(self, node=None):
        # 没有传就删除尾部节点
        if not node:
            node = self.tail
        if node == self.tail:
            return self.__remove_tail()
        elif node == self.head:
            return self.__remove_head()
        else:
            print(node)
            # 把当前节点的上个节点引用指向下个节点
            node.prev.next = node.next
            # 把当前节点的下个节点引用指向上个节点
            node.next.prev = node.prev
            self.size -= 1
            return node

    # 删除尾部节点
    def __remove_tail(self):
        if not self.tail:
            return
        # 尾部节点
        node = self.tail
        if node.prev:
            # 设置尾部节点的引用
            self.tail = node.prev
            self.tail.next = None
        else:
            # 说明没有上个节点，只有一个节点，把头部和尾部设置为空
            self.head = self.next = None
        self.size -= 1
        return node

    def __remove_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            self.head = node.next
            self.head.prev = None
        else:
            self.head = self.next = None
        self.size -= 1
        return node

    def push(self, node):
        return self.__push(node)

    def pop(self):
        return self.__remove_tail()

    def shift(self):
        return self.__remove_head()

    def unshift(self, node):
        return self.__unshift(node)

    def remove(self, node=None):
        return self.__remove(node)

    def __repr__(self):
        p = self.head
        line = ''
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += '=>'
        return line


if __name__ == '__main__':
    print('当前文件入口')
    lists = DoubleLinkedList(2)

    a = [Node(x, x) for x in range(10)]
    a.append(Node('xiaofeng', 'dage'))

    lists.unshift(a[1])
    lists.unshift(a[2])
    lists.push(a[4])
    lists.unshift(a[3])
    lists.shift()
    lists.remove(a[1])
    lists.pop()
    # lists.add(a[9])
    print(lists, 'asd')
