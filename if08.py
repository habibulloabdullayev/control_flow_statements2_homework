def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number==1:
        print('monday')
    if number==2:
        print('tuesday')
    if number==3:
        print('wednesday')
    if number==4:
        print('thursday')
    if number==5:
        print('friday')
    if number==6:
        print('saturday')
    if number==7:
        print('sunday')
    return ' '
print(main(2))
print(main(6))