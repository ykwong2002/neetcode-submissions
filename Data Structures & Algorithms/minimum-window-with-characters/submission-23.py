class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        # Create freq array of t
        freq_t = {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        
        # Sliding window for s
        freq_s = {}
        l = 0
        shortest = len(s) + 1
        shortest_substring = ""
        have = 0
        need = len(freq_t)
        
        for r in range(len(s)):
            char = s[r]
            if char in freq_t:
                freq_s[char] = freq_s.get(char, 0) + 1
                if freq_s[char] == freq_t[char]:
                    have += 1
            
            # If/While t is in s, shrink sliding window
            while have == need:
                if (r - l + 1) < shortest:
                    shortest = r - l + 1
                    shortest_substring = s[l : r + 1]
                
                left_char = s[l]
                if left_char in freq_t:
                    if freq_s[left_char] == freq_t[left_char]:
                        have -= 1
                    freq_s[left_char] -= 1
                l += 1
        
        return shortest_substring