def mycombinations(arr, n, i, combo, result):
    if n == 0:
        result.append(combo[:])
        return
    if i == len(arr):
        return
    combo.append(arr[i])
    mycombinations(arr, n-1, i+1, combo, result)
    combo.pop()
    mycombinations(arr, n, i+1, combo, result)

arr = [1, 2, 3, 4]
result = []
for i in range(1, len(arr)+1):
    mycombinations(arr, i, 0, [], result)

for combo in result:
    print(combo)

