# Ex8
def extract_even(lst):
    result = []
    for number in lst:
        if number % 2 == 0:
            result.append(number)
    return result