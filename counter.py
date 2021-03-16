profit_dict = {}
for _ in range(int(input())):
    size, profit = map(int, input().split(" "))
    profit_dict[size] = profit

print(profit_dict)
