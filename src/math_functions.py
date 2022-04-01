#Implement math functions here
def addition(addend1, addend2):
    """Returns addition of addend1 and addend2
    \n(addend1 + addend2)"""
    pass

def subtract(minuend, subtrahend):
    """Returns subtraction of minuend and subtrahend
    \n(minuend - subtrahend)"""
    pass

def multiply(multiplicand, multiplayer):
    """Returns multiplication of multiplicand and multiplayer
    \n(multiplicand * multiplayer)"""
    pass

def divide(divident, divisor):
    """Returns division of divident and divisor
    \n(divident / divisor)
    \nDivisien by zero prints error on stderr"""
    pass

def exponentiate(base, exponent):
    """Returns power of base and exponent
    \n(base ** exponent)"""
    pass
    if exponent < 0:
        raise ValueError("Exponent lower than 0")
    return (base ** exponent)

def nthroot(base, radicand):
    """Returns nth root of base and radicand
    \n(base ** (1/radicand))
    \nAny root from base < 0 prints error on stderr"""
    pass

def factorial(number):
    """Returns factorial of number
    \n(number!)
    \nAny factorial from number < 0 prints error on stderr"""
    if type(number) != int:
        raise ValueError("Integer number expected")
    if number < 0:
        raise ValueError("Factorial exists for positive numbers only")
    if number == 0:
        return 1

    if number == 1:
        return number
    return number*factorial(number-1)
    pass

def absolute(number):
    """Returns absolute value of number
    \n(|number|)"""
    if number < 0:
        return -number
    if number >= number:
        return number
    pass