
def fizz_buzz(num):
    """Returns 'Fizz', 'Buzz', 'FizzBuzz', or the argument 
       it receives, all depending on the argument
    Args:
        num: a positive integer

    Returns:
        returns a string 'Fizz' if num is divisible by 3
        returns a string 'Buzz' if num is divisible by 5
        returns a string 'FizzBuzz' if num is divisible by 3 and 5
        returns num if num is not divisible by 3 0r 5
    """
    try:
        if num < 0 or not isinstance(num, int):
            return 'Invalid argument: {}'.format(num)
    except(TypeError):
        return 'Invalid argument: {}'.format(num)

    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num

