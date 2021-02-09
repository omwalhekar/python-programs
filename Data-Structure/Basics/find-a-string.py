def count_substring(string, sub_string):
    count = 0
    l = len(string)
    l_sub = len(sub_string)
    for i in range(l-l_sub+1):
        if(sub_string in string[i:i+l_sub]):
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
