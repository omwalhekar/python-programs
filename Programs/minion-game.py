def isVowel(ch):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return ch in vowels


def getVowelStrings(index, string, kevin):
    return([s[index:i+1]
            for i in range(index, len(string)) if s[index:i+1] not in kevin])


def getConsonantStrings(index, string, stuart):
    return([s[index:i+1]
            for i in range(index, len(string)) if s[index:i+1] not in stuart])


def countSubstrings(ch, string):
    n = len(string)
    l = len(ch)
    i = 0
    cnt = 0
    for k in range(0, n-l+1):
        if(ch in string[k:k+l]):
            cnt += 1
    return cnt


def minion_game(string):
    kevin = []
    stuart = []
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if(isVowel(string[i])):
            kevin += getVowelStrings(i, string, kevin)
        else:
            stuart += getConsonantStrings(i, string, stuart)

    for s in kevin:
        kevin_score += countSubstrings(s, string)
    for s in stuart:
        stuart_score += countSubstrings(s, string)

    if(stuart_score < kevin_score):
        print("Kevin " + str(kevin_score))
    elif(stuart_score == kevin_score):
        print("Draw")
    else:
        print("Stuart " + str(stuart_score))


if __name__ == '__main__':
    s = input()
    minion_game(s)
