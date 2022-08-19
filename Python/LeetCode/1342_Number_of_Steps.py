def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """

    '''
    Input: num = 14
    Output: 6
    Explanation: 
    Step 1) 14 is even; divide by 2 and obtain 7. 
    Step 2) 7 is odd; subtract 1 and obtain 6.
    Step 3) 6 is even; divide by 2 and obtain 3. 
    Step 4) 3 is odd; subtract 1 and obtain 2. 
    Step 5) 2 is even; divide by 2 and obtain 1. 
    Step 6) 1 is odd; subtract 1 and obtain 0.
    '''

    processedNum = num

    stepCounter = 0

    while processedNum != 0:

        #is even?
        if processedNum%2 == 0:

            processedNum = processedNum/2

        else:

            processedNum -= 1

        stepCounter += 1

    return stepCounter

print(numberOfSteps(14))
