def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    if n//10000>(n//1000)%10 and (n//10000>(n//100)%10 and (n//10000>(n//10)%10 and n//10000>n%10)):
        print(n//10000)
    if (n//1000)%10>n//10000 and ((n//1000)%10>(n//100)%10 and ((n//1000)%10>(n//10)%10 and (n//1000)%10>n%10)):
        print((n//100)%10)
    if (n//100)%10>n//10000 and ((n//100)%10>(n//1000)%10 and ((n//100)%10>(n//10)%10 and (n//100)%10>n%10)):
        print((n//10)%100)
    if (n//10)%10>n//10000 and ((n//10)%10>(n//1000)%10 and ((n//10)%10>(n//100)%10 and (n//10)%10>n%10)):
        print((n//10)%10)
    if n%10>n//10000 and (n%10>(n//1000)%10 and (n%10>(n//100)%10 and n%10>(n//10)%10)):
        print(n%10)
    return ' '
print(main(23546))