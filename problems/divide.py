def divide(dividend: int, divisor: int) -> int:
    MAX = 2**31 - 1
    MIN = -2**31
    if (dividend == 2**31 and divisor == -1):
        return (-dividend) - 1
    is_neg: bool = (divisor < 0) ^ (dividend < 0)
    if (dividend == 0):
        return 0
    my_divisor = abs(divisor)
    my_dividend = abs(dividend)
    if (my_divisor == 1):
        return min(max(-my_dividend if is_neg else my_dividend, MIN), MAX)
    
    quotient: int = 0
    while (my_dividend >= my_divisor):
        q = 0
        while (my_dividend >= (my_divisor << q)):
            q += 1
        
        q -= 1
        quotient += 1 << q
        my_dividend -= my_divisor << q
    return min(max(-quotient if is_neg else quotient, MIN), MAX)

print(divide(1, -1))