#!/usr/bin/env python3

def simple_text_editor(operations):
    stack = []
    s = ""

    for operation in operations:
        operation = operation.split()

        if operation[0] == '4':
            s = stack.pop()
            continue
        elif operation[0] == '1':
            stack.append(s)
            s += operation[1]
        elif operation[0] == '2':
            stack.append(s)
            s = s[:len(s)-int(operation[1])]
        elif operation[0] == '3':
            print(s[int(operation[1])-1])
        else:
            raise ValueError("Invalid operation")


if __name__ == "__main__":
    num_operations = int(input())
    operations = []
    for i in range(num_operations):
        operations.append(input())

    simple_text_editor(operations)

