#!/usr/bin/env python
# coding=utf-8


from biginteger import BigInteger


first = BigInteger("12345")
second = BigInteger("6789")


print(first, "==", second, "=", first == second)
print(first, "!=", second, "=", first != second)
print(first, "<", second, "=", first < second)
print(first, ">", second, "=", first > second)
print(first, "<=", second, "=", first <= second)
print(first, ">=", second, "=", first >= second)
print(first, "+", second, "=", first + second)
print(first, "-", second, "=", first - second)
print(first, "//", second, "=", first // second)
print(first, "*", second, "=", first * second)
print(first, "%", second, "=", first % second)
print(first, "**", second, "=", first ** second)
print(first, "|", second, "=", first | second)
print(first, "&", second, "=", first & second)
print(first, "^", second, "=", first ^ second)
print(first, "<<", second, "=", first << second)
print(first, ">>", second, "=", first >> second)
