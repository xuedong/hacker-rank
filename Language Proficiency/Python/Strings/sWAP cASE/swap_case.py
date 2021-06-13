def swap_case(s):
    result = ''.join([ch.upper() if ch.islower() else ch.lower() for ch in s])
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

