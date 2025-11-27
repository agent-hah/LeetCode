def earliestFinishTime(landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
    minimum = 2 ** 31 - 1

    for landRideIdx in range(len(landStartTime)):
        duration = landStartTime[landRideIdx] + landDuration[landRideIdx]
        for waterRideIdx in range(len(waterStartTime)):
            newDuration = duration + (waterStartTime[waterRideIdx] - duration) + waterDuration[waterRideIdx] if waterStartTime[waterRideIdx] > duration else duration + waterDuration[waterRideIdx]
            minimum = min(minimum, newDuration)
    
    for waterRideIdx in range(len(waterStartTime)):
        duration = waterStartTime[waterRideIdx] + waterDuration[waterRideIdx]
        for landRideIdx in range(len(landStartTime)):
            newDuration = duration + (landStartTime[landRideIdx] - duration) + landDuration[landRideIdx] if landStartTime[landRideIdx] > duration else duration + landDuration[landRideIdx]
            minimum = min(minimum, newDuration)
    return minimum


print(earliestFinishTime([2,8], [4,1], [6], [3]))
dict = {1:2}

print(1 in dict)