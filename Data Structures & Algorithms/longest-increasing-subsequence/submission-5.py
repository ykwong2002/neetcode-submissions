class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        # initialise dp array
        dp = [1] * n

        # build dp array from start
        for i in range(n):
            print("i:", i)
            for j in range (i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                print(dp)
        
        return max(dp)
"""
1   2   1   3   3   4
Goal: return integer (length of longest increasing subsequence)
- subsequence: need not be side by side, can be apart --> BUT must be increasing
- constant transition --> DP
- initialise dp array to all 1 (since each letter is a LIS)
- dp array --> stores length of longest increasing subsequnce up until index i
- iterate through each number: (for loop)
    - check all previous numbers to see if it is lower (for loop)
    - if lower, add 1 to the dp[lower number]

0   1   2   3   4   5   6
9   1   4   2   3   3   7
        i
j
1   1   1   1   1   1   1
"""