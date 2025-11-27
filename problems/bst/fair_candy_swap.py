def fairCandySwap(aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
    sumAlice = sum(aliceSizes)
    sumBob = sum(bobSizes)

    aliceRef = set(aliceSizes)
    bobSizes.sort()
    
    for i in aliceRef:
        l = 0
        r = len(bobSizes) - 1

        while l <= r:
            complement = (sumBob - sumAlice + 2 * i) // 2
            if complement < 0:
                break
            m = l + (r - l) // 2

            if bobSizes[m] == complement:
                return [i, complement]
            elif bobSizes[m] > complement:
                r = m - 1
            else:
                l = m + 1
    return []

print(fairCandySwap([1], [2, 3]))
print(fairCandySwap([1,2,5], [2,4]))
print(fairCandySwap([35,17,4,24,10], [63,21]))
print(fairCandySwap([32,38,8,1,9], [68,92] ))