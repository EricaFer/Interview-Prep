def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    commonPrefix = []

    for index in range(0,201):

        prefixPerIndex = []

        try:

            for splittedString in strs:

                prefixPerIndex.append(splittedString[index])

        except IndexError:

            break

        if len(list(set(prefixPerIndex))) == 1:

            commonPrefix.append(prefixPerIndex[0])

        else:
            break

    return ''.join(commonPrefix)

print(longestCommonPrefix(["dog","racecar","car"]))
