# def power(x, y):
#     if(y == 0):
#         return 1
#     elif(y % 2 == 0):
#         return power(x, y//2)*power(x, y//2)
#     else:
#         return x*power(x, y//2)*power(x, y//2)

def power(x, y):
    if(y == 0):
        return 1
    else:
        hPower = power(x, y//2)
        if(y % 2 == 0):
            return hPower*hPower
        else:
            return x*hPower*hPower


print(power(2, 10))
