#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Person(name={}, age={})".format(self.name, self.age)

    def __str__(self):
        return "My name is {}, I'm {} years old.".format(self.name, self.age)


class Teacher(Person):
    def __init__(self, name, age, std_num):
        super().__init__(name, age)
        self.std_num = std_num

    def __str__(self):
        return "My name is {}, I'm {} years old. I am a teacher, I have {} students.".format(
            self.name, self.age, self.std_num
        )


def main():
    t1 = Teacher("Alex", 18, 1000000)
    print(t1)


if __name__ == "__main__":
    main()
