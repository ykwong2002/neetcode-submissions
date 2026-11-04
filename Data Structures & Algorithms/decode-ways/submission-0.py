class Solution:
    def numDecodings(self, s: str) -> int:
        # cache (index : no. of ways pairing)
        dp = {len(s) : 1} # only 1 way to decode the final digit

        def dfs(i):
            # cached case
            if i in dp:
                return dp[i]
            # if leading 0, not valid
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)
