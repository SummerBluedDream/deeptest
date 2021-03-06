'''

概述

什么是队列，简单而言：先进先出。

队列是一种特殊的线性表，特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作，和栈一样，队列是一种操作受限制的线性表。

进行插入操作的端称为队尾，进行删除操作的端称为队头。

队列中没有元素时，称为空队列。

队列的数据元素又称为队列元素。

在队列中插入一个队列元素称为入队，从队列中删除一个队列元素称为出队。

因为队列只允许在一端插入，在另一端删除，所以只有最早进入队列的元素才能最先从队列中删除，故队列又称为先进先出（FIFO—first in first out）线性表。

'''


class Queue:
    def __init__(self, size=30):
        # 初始化队列长度
        self.size = size

        # 初始化队列列表
        self.queue = []

        # 初始化队列前端、后端位置
        self.front = 0
        self.rear = -1

    # 判断队列是否为空
    def is_empty(self):
        return self.rear == 0

    # 判断队列是否满了
    def is_full(self):
        res = False
        if (self.rear - self.front + 1) == self.size:
            res = True

        return res

        # 入队

    def add(self, obj):
        if self.is_full():
            raise Exception("我去，队列满了……")
        else:
            self.queue.append(obj)
            self.rear += 1

    # 出队
    def delete(self):
        if self.is_empty():
            raise Exception("队列是空的，出不了了……")
        else:
            self.rear -= 1
            self.queue.pop(0)

            # 队列头元素

    def first(self):
        if self.is_empty():
            raise Exception("队列是空的啦……")
        else:
            return self.queue[self.front]

            # 队列尾元素

    def last(self):
        if self.is_empty():
            raise Exception("队列是空的啦……")
        else:
            return self.queue[self.rear]

            # 打印队列

    def show(self):
        print(self.queue)


if __name__ == "__main__":

    print("队列实现示例")

    # 初始化长度为5的队列
    queue = Queue(5)

    # 先把1-5的数据入队
    for index in range(1, 6):
        queue.add(index)

        # 打印下队列数据
    queue.show()

    # 打印下队列头
    print(queue.first())

    # 打印下队列尾
    print(queue.last())

    # 出个队试试
    queue.delete()

    # 打印下队列看下是否出队了
    queue.show()

    # 再出个队试试
    queue.delete()

    # 打印下队列看下是否出队了
    queue.show()
'''
队列的关键点：

先进先出
注意溢出的处理
 

'''
