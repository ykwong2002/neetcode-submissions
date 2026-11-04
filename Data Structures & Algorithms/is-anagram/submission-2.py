class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create hashtable of count of letters
        count = [0] * 26

        # use count to count letters in s
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # use t to remove letters in count
        for char in t:
            count[ord(char) - ord('a')] -= 1

        # check if there is a non-empty letter count
        for num in count:
            if num != 0:
                return False
        return True