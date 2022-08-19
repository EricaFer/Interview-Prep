def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """

    # unpacks string - LeetCode does not accept
    #magazineList = [*magazine]

    magazineList = [x for x in magazine]

    for ransomLetter in ransomNote:

        if ransomLetter in magazineList:

            magazineList.remove(ransomLetter)

        else:
            
            return 'false'

    return 'true'

print(canConstruct(ransomNote = "aa", magazine = "aab"))