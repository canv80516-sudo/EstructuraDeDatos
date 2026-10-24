from abc import ABC, abstractmethod


class Order:
    def __init__(self, qtty, customer):
        self.__customer = customer
        self.__qtty = qtty

    def print(self):
        print("     Customer:", self.getCustomer())
        print("     Quantity:", self.getQtty())
        print("     ------------")

    def getQtty(self):
        return self.__qtty

    def getCustomer(self):
        return self.__customer


class Node:
    def __init__(self, info):
        self.__info = info
        self.__next = None

    def getInfo(self):
        return self.__info

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next


class QueueInterface(ABC):

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def front(self):
        pass

    @abstractmethod
    def enqueue(self, info):
        pass

    @abstractmethod
    def dequeue(self):
        pass



class Queue(QueueInterface):
    def __init__(self):
        self.__top = None
        self.__tail = None
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.__top.getInfo()

    def enqueue(self, info):
        node = Node(info)
        if self.isEmpty():
            self.__top = node
        else:
            self.__tail.setNext(node)
        self.__tail = node
        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        info = self.__top.getInfo()
        self.__top = self.__top.getNext()
        self.__size -= 1
        if self.__top is None:
            self.__tail = None
        return info

    def printInfo(self):
        print("********* QUEUE DUMP *********")
        print("  Size:", self.__size)
        node = self.__top
        i = 1
        while node is not None:
            print("  ** Element", i)
            node.getInfo().print()
            node = node.getNext()
            i += 1
        print("******************************")

    def getNth(self, pos):
        if pos < 1 or pos > self.__size:
            return None
        node = self.__top
        for _ in range(pos - 1):
            node = node.getNext()
        return node.getInfo()


def main():
    q = Queue()
    q.printInfo()

    q.enqueue(Order(20, "cust1"))
    q.printInfo()
    q.enqueue(Order(30, "cust2"))
    q.printInfo()
    q.enqueue(Order(40, "cust3"))
    q.printInfo()
    q.enqueue(Order(50, "cust3"))
    q.printInfo()

    print("Front:")
    q.front().print()
    q.printInfo()

    print("Dequeue:")
    q.dequeue().print()
    q.printInfo()

    print("Elemento 3:")
    q.getNth(3).print()
    print("Posición inválida:", q.getNth(10))


if __name__ == "__main__":
    main()