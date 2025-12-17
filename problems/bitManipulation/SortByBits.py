def sortByBits(arr: list[int]) -> list[int]:
    arr.sort(key= lambda x: (bin(x)[2::].count("1"), x), reverse=False)
    return arr

print(sortByBits([0,1,2,3,4,5,6,7,8]))
print(sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))