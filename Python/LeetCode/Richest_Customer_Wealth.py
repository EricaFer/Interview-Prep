def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """

    customersWealth = []

    for i in range(0,len(accounts)):

        customersWealth.append(sum(accounts[i]))

    return max(customersWealth)

print(maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]]))
