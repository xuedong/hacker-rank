vowels = "AEIOU"

def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0

    for i in range(len(s)):
        if s[i] in vowels:
            kevin_score += len(s) - i
        else:
            stuart_score += len(s) - i

    if kevin_score > stuart_score:
        print("Kevin "+str(kevin_score))
    elif stuart_score > kevin_score:
        print("Stuart "+str(stuart_score))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

