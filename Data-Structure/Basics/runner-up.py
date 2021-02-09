arr = [5, 4, 6, 6, 3]
n = 5
maxi = max(arr)
new_arr = [arr[x] for x in range(0, n) if(arr[x] < maxi)]
print(max(new_arr))
