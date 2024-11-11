if __name__ == '__main__':
    #双链表

    # 双链表的结点类
    class Node(object):

        def __init__(self, elem):
            # _elem存放数据元素
            self.elem = elem
            # _next是下一个节点的标识
            self.pre = None
            self.next = None

    #双链表类
    class DoubleLinkList():

            #初始化
            def __init__(self):
                self._head = None

            #判断链表是否为空
            def is_empty(self):
                return self._head == None

            #链表长度
            def length(self):
                count = 0
                #设置当前位置cur,和头指针指向的位置相同
                cur = self._head
                #如果列表为空。返回长度0
                if self.is_empty():
                    return 0
                while cur != None:
                    count += 1
                    cur = cur.next
                return count

            #遍历链表
            def travel(self):
                if self.is_empty():
                    return
                cur = self._head
                while cur != None:
                    print(cur.elem)
                    cur = cur.next

            # 在列表的头部插入结点（头插法)
            def add(self, item):
               node = Node(item)
               if self.is_empty():
                  self._head = node
               node.next = self._head
               self._head = node
               node.next.pre = node

            #尾部插入结点(尾插法)

            # 在列表的尾部插入结点（尾插法)
            def append(self,item):
                #新建一个结点,传入参数
                node = Node(item)
                #列表为空直接尾部就是头部
                if self.is_empty():
                    self._head = node
                else:
                    cur = self._head
                    while cur.next != None:
                        cur = cur.next
                    #当while判断cur指向最后一个结点的时候
                    cur.next = node
                    node.pre = cur

            #在具体位置插入结点,pos为插入的位置
            def insert(self,pos,item):
                cur = self._head
                node = Node(item)
                count = 0
                if pos <= 0:
                    # 如果插入的位置<=0,直接调用头插法
                    self.add(item)
                elif pos >= (self.length()-1):
                    # 如果插入的位置>=列表的长度,直接调用尾插法
                    self.append(item)
                else:
                    #其他情况就是在列表中间插入结点
                    while count < pos:
                        count += 1
                        cur = cur.next
                    node.next = cur
                    node.pre = cur.pre
                    cur.pre.next = node
                    cur.pre = node

            #删除元素

            #删除结点
            def remove(self,item):
                cur = self._head
                while cur != None:
                    if cur.elem == item:
                        if cur == self._head:
                            self._head = cur.next
                            if cur.next:
                                #判断链表是否只有一个结点
                                cur.next.pre = None
                        else:
                            cur.pre.next = cur.next
                            if cur.next:
                                cur.next.pre = cur.pre
                        break
                    else:
                        cur = cur.next

                #空列表不需要删除结点
                if self.is_empty():
                    return

            #查找元素
            def serch(self,item):
                cur = self._head
                while cur != None :
                    if cur.elem == item:
                        return True
                    else:
                        cur = cur.next
                return False

    double = DoubleLinkList()
