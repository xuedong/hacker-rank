def print_formatted(number):
    # your code goes here
    width = len("{:b}".format(n))
    for i in range(1, n+1):
        print("{0:{width}d}".format(i, width=width) + " " + "{0:{width}o}".format(i, width=width) + " " + "{0:{width}X}".format(i, width=width) + " " + "{0:{width}b}".format(i, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

