def mySqrt(x: int) -> int:
        l: int = 1
        r: int = x // 2 + 1
        while l < r:
            m: int = l + (r - l) // 2
            val = m * m
            if val == x:
                return m
            elif x < val:
                r = m - 1
            else:
                l = m + 1
        return l - 1 if l * l > x else l