#!/usr/bin/env python3

from collections import namedtuple


if __name__ == "__main__":
    N = int(input())
    fields = input().split()

    total = 0
    for i in range(N):
        Student = namedtuple('student', fields)
        field1, field2, field3, field4 = input().split()
        student = Student(field1, field2, field3, field4)
        total += int(student.MARKS)
    print(total/N)

