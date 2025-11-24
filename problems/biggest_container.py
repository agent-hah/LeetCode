def maxArea(height: list[int]) -> int:
        left = 0
        maxArea = 0
        while (left < len(height)):
            for right in range(left, len(height)):
                width = right - left
                tall_ith: int = min(height[left], height[right])
                maxArea = max(maxArea, (width * tall_ith))
            left += 1
        return maxArea