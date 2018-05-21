from node import TwoWayNode


class BigInteger(object):
    """A class-representation of a big integer ADT (two-way nodes)."""
    def __init__(self, init_value="0"):
        self._head = TwoWayNode(init_value[0])
        self._tail = self._head
        self.negative = True if int(init_value) < 0 else False
        self.size = len(init_value)
        for i in range(1, len(init_value)):
            self._tail.next = TwoWayNode(int(init_value[i]), self._tail)
            self._tail = self._tail.next

    def to_string(self):
        """
        Returns the two-way node as a string.
        :return str: sring representation of the node. 
        """
        string = ""
        node = self._head
        while node is not None:
            string += str(node.data)
            node = node.next
        return string

    def __eq__(self, other):
        """
        self == other
        """
        result = True
        node1 = self._head
        node2 = other._head
        if self.negative != other.negative:
            return False
        else:
            while node1 is not None and node2 is not None:
                result = False if node1.data != node2.data else True
                if not result:
                    return result
                node1 = node1.next
                node2 = node2.next
            if node1 is not None or node2 is not None:
                return False
        return result

    def __ne__(self, other):
        """
        self != other
        """
        return not self == other

    def __lt__(self, other):
        """
        self < other
        """
        node1 = self._head
        node2 = other._head
        if self.negative and not other.negative:
            return True
        elif not self.negative and other.negative:
            return False
        else:
            while node1 is not None and node2 is not None:
                result = False if node1.data > node2.data else True
                if not result:
                    return result
                node1 = node1.next
                node2 = node2.next
            if node1 is not None and node2 is None:
                return False
        return True

    def __gt__(self, other):
        """
        self > other
        """
        return (not self < other) and self != other

    def __le__(self, other):
        """
        self <= other
        """
        return self < other or self == other

    def __ge__(self, other):
        """
        self >= other
        """
        return (not self < other) or self == other

    def __add__(self, other):
        """
        self + other
        """
        new_big_integer = ""
        if self.negative != other.negative:
            if self.negative:
                new_big_other_integer = BigInteger(self.to_string())
                new_big_other_integer.negative = False
                return other - self
            elif other.negative:
                new_big_other_integer = BigInteger(other.to_string())
                new_big_other_integer.negative = False
                return self - other
        elif self.negative == other.negative and self.negative:
            new1 = BigInteger(self.to_string())
            new1.negative = False
            new2 = BigInteger(other.to_string())
            new2.negative = False
            new_big_integer = BigInteger(str(self + other))
            new_big_integer.negative = True
            return new_big_integer
        elif self.negative == other.negative and not other.negative:
            if self.size > other.size:
                while self.size != other.size:
                    other._head.previous = TwoWayNode(0, None, other._head)
                    other._head = other._head.previous
                    other.size += 1
                new_big_integer = self._add(other)
                other._rem_zeros()
            elif self.size < other.size:
                while self.size != other.size:
                    self._head.previous = TwoWayNode(0, None, self._head)
                    self._head = self._head.previous
                    self.size += 1
                new_big_integer = self._add(other)
                self._rem_zeros()
            elif self.size == self.size:
                new_big_integer = self._add(other)
            return new_big_integer

    def _rem_zeros(self):
        """
        Removes zeros on the beginning of the number.
        """
        cur = self._head
        if cur.data == 0:
            while self.size != 1 and cur.data == 0:
                self.size -= 1
                self._head = self._head.next
                cur = self._head

    def _add(self, other):
        """
        Helper method for __add__().
        """
        new_big_integer = ""
        node1 = self._tail
        node2 = other._tail
        tmp = 0
        while node1 is not None or node2 is not None:
            number = int(node1.data) + int(node2.data) + tmp
            tmp = 0
            if len(str(number)) == 2:
                tmp = number // 10
                number %= 10
            node1 = node1.previous
            node2 = node2.previous
            new_big_integer += str(number)
        new_big_integer = new_big_integer[::-1]
        return new_big_integer

    def __sub__(self, other):
        """
        self - other
        """
        first = ("-" + self.to_string()) if self.negative else self.to_string()
        second = ("-" + other.to_string()) if other.negative else other.to_string()
        new_big_integer = BigInteger(str(int(first) - int(second)))
        return new_big_integer

    def __mul__(self, other):
        """
        self * other
        """
        first = ("-" + self.to_string()) if self.negative else self.to_string()
        second = ("-" + other.to_string()) if other.negative else other.to_string()
        new_big_integer = BigInteger(str(int(first) * int(second)))
        return new_big_integer

    def __floordiv__(self, other):
        """
        self // other
        """
        first = ("-" + self.to_string()) if self.negative else self.to_string()
        second = ("-" + other.to_string()) if other.negative else other.to_string()
        new_big_integer = BigInteger(str(int(first) // int(second)))
        return new_big_integer

    def __mod__(self, other):
        """
        self % other
        """
        first = ("-" + self.to_string()) if self.negative else self.to_string()
        second = ("-" + other.to_string()) if other.negative else other.to_string()
        new_big_integer = BigInteger(str(int(first) % int(second)))
        return new_big_integer

    def __pow__(self, other, modulo=None):
        """
        self ** other
        """
        new_big_integer = BigInteger("1")
        if not other.negative:
            for i in range(0, int(other.to_string())):
                new_big_integer = new_big_integer * self
        elif other.negative:
            new_big_integer = 1 // int(new_big_integer.to_string())
        return new_big_integer

    def __or__(self, other):
        """
        self | other
        """
        first = ("-" + self.to_string()) if self.negative else self.to_string()
        second = ("-" + other.to_string()) if other.negative else other.to_string()
        new_big_integer = BigInteger(str(int(first) | int(second)))
        return new_big_integer

    def __and__(self, other):
        """
        self & other
        """
        first = ("-" + self.to_string()) if self.negative else self.to_string()
        second = ("-" + other.to_string()) if other.negative else other.to_string()
        new_big_integer = BigInteger(str(int(first) & int(second)))
        return new_big_integer

    def __xor__(self, other):
        """
        self ^ other
        """
        first = ("-" + self.to_string()) if self.negative else self.to_string()
        second = ("-" + other.to_string()) if other.negative else other.to_string()
        new_big_integer = BigInteger(str(int(first) ^ int(second)))
        return new_big_integer

    def __lshift__(self, other):
        """
        self << other
        """
        new_big_integer = self * BigInteger(str(2 ** int(other.to_string())))
        return new_big_integer

    def __rshift__(self, other):
        """
        self >> other
        """
        new_big_integer = self // BigInteger(str(2 ** int(other.to_string())))
        return new_big_integer

    def __str__(self):
        """
        Returns str for print() function.
        """
        return self.to_string()
