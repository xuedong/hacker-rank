import string
alphabet = string.ascii_lowercase


def print_rangoli(size):
    # your code goes here
    patterns = []
    for i in range(n):
        pattern = '-'.join(alphabet[i:n])
        patterns.append((pattern[::-1]+pattern[1:]).center(4*n-3, '-'))
    print('\n'.join(patterns[::-1]+patterns[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

