#!/usr/bin/env python3


def count_substring(string, sub_string):
    str_len = len(string)
    sub_len = len(sub_string)
    count = 0
    for i in range(str_len-sub_len+1):
        if sub_string == string[i:(i+sub_len)]:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

