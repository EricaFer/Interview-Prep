def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romanConversion = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    integersSum = []

    for index,numeral in enumerate(s):
        
        integersSum.append(romanConversion[numeral])

        try:
            if integersSum[index] > integersSum[index-1]:

                integersSum[index-1] = -1 * integersSum[index-1]

        except IndexError:

            pass
    
    return sum(integersSum)

print(romanToInt(s = "MCMXCIV"))



