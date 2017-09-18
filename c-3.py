#!/usr/bin/python

import unittest

# return a number 10
def test():
	book1.test

# return a list
def f2():
	return range(10);

# return the first three letter of a string
def f3(s):
	return s[0:3];

# compare two number
def f4(n1, n2):
	return (n1 > n2);

if __name__ == "__main__":
	print test();
	print f2();
	print f3('Hello');
	print f4(10, 20);
