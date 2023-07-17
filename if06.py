def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    if n//10000>(n//1000)%10 and (n//10000>(n//100)%10 and (n//10000>(n//10)%10 and n//10000>n%10)):
        print(5)
    if (n//1000)%10>n//10000 and ((n//1000)%10>(n//100)%10 and ((n//1000)%10>(n//10)%10 and (n//1000)%10>n%10)):
        print(4)
    if (n//100)%10>n//10000 and ((n//100)%10>(n//1000)%10 and ((n//100)%10>(n//10)%10 and (n//100)%10>n%10)):
        print(3)
    if (n//10)%10>n//10000 and ((n//10)%10>(n//1000)%10 and ((n//10)%10>(n//100)%10 and (n//10)%10>n%10)):
        print(2)
    if n%10>n//10000 and (n%10>(n//1000)%10 and (n%10>(n//100)%10 and n%10>(n//10)%10)):
        print(1)
    return ' '
print(main(76514))
print(main(54694))