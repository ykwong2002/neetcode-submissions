class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}

/*
n = 4
dp[i] = num of ways to reach idx i

dp[i] = dp[i-1] + dp[i-2]
dp:     0   1   2   0   0
idx:    0   1   2   3   4

1111
211
121
112
22


*/