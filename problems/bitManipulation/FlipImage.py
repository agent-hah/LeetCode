def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
    for row in image:
        row.reverse()
        for i in range(len(row)):
            row[i] ^= 1
    return image


print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

print(list("hello"))