def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """ 
    if a==b:
        print(0)
    if a>b:
        print(a)
    if b>a:
        print(b)
    return ' '
print(main(3,7))
print(main(5,5))