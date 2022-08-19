def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """

    returnedList = []

    for num in range(1,n+1):

        result = ''

        if num%3 == 0:

            result += 'Fizz'

        if num%5 == 0:

            result += 'Buzz'

        if result == '':

            result = str(num)

        returnedList.append(result)

    return returnedList

print(fizzBuzz(15))
