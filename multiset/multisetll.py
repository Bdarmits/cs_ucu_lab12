from node import *
import copy

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None
        self.size = 0

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest
        self.size += 1

    def delete(self, value):
        """
        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next
        self.size -= 1

    def remove_all(self):
        """
        Removes all nodes from the multiset and returns values as a list.
        """
        value = self._head.item
        self._head = None
        self.size = 0
        return value


    def __len__(self):
        return self.size

    def split_half(self):
        # m2 = Multiset()
        # counter = 0
        # multiset_copy = copy.deepcopy(self)
        # while multiset_copy._head != None:
        #     multiset_copy._head = multiset_copy._head.next
        #     counter += 1
        # if counter == 1:
        #     return None
        # for i in range(counter // 2):
        #     m2.add(self._head)
        #     self._head = self._head.next
        # return self, m2
        current = self._head
        m1 = Multiset()
        m2 = Multiset()
        for i in range(len(self)):
            if i  < len(self) / 2 :
                m1.add(current.item)
            else:
                m2.add(current.item)
            current = current.next
        return m1, m2


if __name__ == "__main__":
    m = Multiset()
    m.add(3)
    m.add("slonik")
    m.add("+")
    print(m.split_half())
    m1, m2 = m.split_half()
    print(3 in m2)
    print(m2.empty())
    print(len(m2))
