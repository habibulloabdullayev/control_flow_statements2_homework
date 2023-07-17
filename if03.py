def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a>b and a<c) or (a>c and a<b):
        print(a)
    if (b>a and b<c) or (b>c and b<a):
        print(b)
    if (c>a and c<b) or (c>b and c<a):
        print(c)
    return ' '
print(main(3,7,1))