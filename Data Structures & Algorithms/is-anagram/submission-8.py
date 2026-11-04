class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Goal: check if number of each letter in s == number of each letter in t
        - create a hashmap for s and t
        - count the values of each letter
        - check if s_dict == t_dict
        """
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        return count == [0] * 26
        # s_dict = {}
        # t_dict = {}

        # for letter in s:
        #     if letter not in s_dict.keys():
        #         s_dict[letter] = 1
        #     else:
        #         s_dict[letter] += 1
        
        # for letter in t:
        #     if letter not in t_dict.keys():
        #         t_dict[letter] = 1
        #     else:
        #         t_dict[letter] += 1

        # return s_dict == t_dict
        