#!/usr/bin/env python
# coding: utf8

import ctypes

class Array():
    def __init__(self,size):
        assert size > 0 , "Arry size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(0)
    def __len__(self):
        return self._size
    def __getitem__(self, index):
        assert index >= 0 and index < self._size, "Array subscript out of range"
        return self._elements[index]
    def __setitem__(self, index, value):
        assert index >= 0 and index < self._size, "Array subscript out of range"
        self._elements[index] = value
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
    def __iter__(self):
        return _ArrayIterator(self._elements)
    # def __iter__(self):
    #     return self

    def next(self):
        self._i = 0
        if self._i < len(self._elements):
            self._i += 1
            return self._elements[self._i]
        else:
            raise StopIteration

    def __repr__(self):
        return "Array(%s)" % (",".join(self._elements))

    def __str__(self):
        theStr = "["
        for i in range(len(self._elements)):
            if i != len(self._elements) - 1:
                theStr += str(self._elements[i]) + ", "
            else:
                theStr += str(self._elements[i])

        return theStr + "]"






class _ArrayIterator :
    def __init__(self,theArray):
        self._arrayRef = theArray
        self._curNdx = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration



class Vector(Array):
    def __add__(self, other):
        arrayl = Array(self._size)
        if len(str(other)) == 1:
            for i,j in enumerate(self._elements):
                arrayl[i] += j + other[0]
        elif len(self) == len(other):
            for i in range(len(self)):
                arrayl[i] = self._elements[i] + other[i]
        else:
            print "type error"
        return arrayl
    def __mul__(self, other):
        arrayl = Array(len(self))
        if len(str(other)) == 1:
            for i,j in enumerate(self):
                arrayl[i] += j * other
        elif len(self) == len(other):
            for i in range(len(self)):
                arrayl[i] = self._elements[i] * other[i]
        else:
            print "type error"
        return arrayl
    def dot(self,other):
        total = 0
        if len(self) == len(other):
            for i in range(len(self)):
                total += self._elements[i] * other[i]
        else:
            print "type error"
        return total


    def __str__(self):
        return str(self._elements)

la1 = Vector(4)
la1[0]=1
la1[1]=2
la1[2]=3
la1[3]=4
la2 = Vector(4)
la2[0]=2
la2[1]=3
la2[2]=4
la2[3]=5
la = la1 + la2
print la
print la[0],la[1],la[2],la[3]
