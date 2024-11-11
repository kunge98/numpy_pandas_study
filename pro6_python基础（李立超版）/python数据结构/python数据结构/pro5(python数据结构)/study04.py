if __name__ == '__main__':
    #单向循环链表

    #单向循环链表的结点类
    class Node(object):

        def __init__(self, elem):
            # _elem存放数据元素
            self.elem = elem
            # _next是下一个节点的标识
            self.next = None

    #单向循环链表类
    class SingleLinkList(object):

            #初始化
            def __init__(self,node = None):
                self._head = None
                if node:
                    node.next = None

            #判断链表是否为空
            def is_empty(self):
                return self._head == None

            #链表长度
            def length(self):
                #count设置的初始值考虑到循环链表没有none值存在
                count = 1
                #设置当前位置cur,和头指针指向的位置相同
                cur = self._head
                #如果列表为空。返回长度0
                if self.is_empty():
                    return 0
                while cur.next != self._head:
                    count += 1
                    cur = cur.next
                return count

            #遍历链表
            def travel(self):
                if self.is_empty():
                    return
                cur = self._head
                while cur.next != self._head:
                    print(cur.elem,end='')
                    cur = cur.next
                print(cur.elem)

            # 在列表的头部插入结点（头插法)

            #添加元素
            def add(self, item):
               node = Node(item)
               cur = self._head
               if self.is_empty():
                  self._head = node
                  node.next = node
               else:
                   while cur.next != self._head:
                        cur = cur.next
                   node.next = self._head
                   self._head = node
                   cur.next = node

            #尾部插入结点(尾插法)
            def append(self,item):
                #新建一个结点,传入参数
                node = Node(item)
                #列表为空直接尾部就是头部
                if self.is_empty():
                    self._head = node
                    node.next = node
                else:
                    cur = self._head
                    while cur.next != self._head:
                        cur = cur.next
                    #当while判断cur指向最后一个结点的时候
                    node.next = self._head
                    cur.next = node

            #在具体位置插入结点,pos为插入的位置
            def insert(self,pos,item):
                node = Node(item)
                count = 0
                pre = self._head
                if pos <= 0:
                    # 如果插入的位置<=0,直接调用头插法
                    self.add(item)
                elif pos >= (self.length()-1):
                    # 如果插入的位置>=列表的长度,直接调用尾插法
                    self.append(item)
                else:
                    #其他情况就是在列表中间插入结点
                    while count < (pos-1):
                        pre = pre.next
                        count += 1
                    node.next = pre.next
                    pre.next = node

            #删除元素
            def remove(self,item):
                cur = self._head
                pre = None
                if self.is_empty():
                    return
                while cur.next != self._head:
                    if cur.elem == item:
                        if cur == self._head:
                            #删除头结点
                            rear = self._head
                            while rear.next != self._head:
                                rear = rear.next
                            self._head = cur.next
                            rear.next = self._head
                        else:
                            #删除中间结点
                            pre.next = cur.next
                        return
                    else:
                        pre = cur
                        cur = cur.next
                #退出循环，删除尾结点
                if cur.elem == item:
                    if cur == self._head:
                        self._head = None
                    else:
                        pre.next = self._head

            #查找元素
            def serch(self,item):
                cur = self._head
                if self.is_empty():
                    return False
                while cur.next != self._head :
                    if cur.elem == item:
                        return True
                    else:
                        cur = cur.next
                if cur.elem == item:
                    return True
                return False
