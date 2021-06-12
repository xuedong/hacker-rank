if __name__ == '__main__':
    n = int(input())
    elements = []
    for _ in range(n):
        string = input().split()
        cmd = string[0]
        args = string[1:]

        if cmd == "print":
            print(elements)
        else:
            cmd += "(" + ",".join(args) + ")"
            eval("elements." + cmd)

