def merge_the_tools(string, k):
    # your code goes here
    # k is length of each substring
    n = len(string)
    parts = n//k
    substrings = []
    # substrings = [string[i:i+k] for i in enumerate(string, parts)]
    j = 0
    for _ in range(parts):
        substrings.append(string[j:j+k])
        j += k

    substrings = list(map(removeRepeatedLetters, substrings))
    print(substrings)


def removeRepeatedLetters(string):
    tempString = ""
    for ch in string:
        if ch not in tempString:
            tempString += ch
    return tempString


if __name__ == '__main__':
    # string, k = input(), int(input())
    string = "AABCAAADA"
    k = 3
    merge_the_tools(string, k)
