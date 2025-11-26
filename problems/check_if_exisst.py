def checkIfExist(arr: list[int]) -> bool:
    arr.sort()

    for i in range(len(arr)):
        l = 0
        r = len(arr) - 1
        target = arr[i] * 2
        while l < r:
            m = l + (r - l) // 2
            
            if m == i:
                l = m + 1
                continue

            if arr[m] == target:
                return True
            elif arr[m] > target:
                r = m - 1
            elif arr[m] < target:
                l = m + 1

        if arr[l] == target and not l == i:
            return True
    return False

print(checkIfExist([10,2,5,3]))