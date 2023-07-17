def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a>c:
        print(a)
    if b>a and b>c:
        print(b)
    if c>a and c>b:
        print(c)
    return '  '
print(main(1,4,2))
print(main(-5,-3,-1))