class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        if m > n:
            smaller = nums2
            bigger = nums1
            smaller_length = n
        else:
            smaller = nums1
            bigger = nums2
            smaller_length = m

        # FIX 1: partition index range is [0, smaller_length]
        l, r = 0, smaller_length

        while True:
            # FIX 2: smaller_med is a PARTITION INDEX
            smaller_med = (l + r) // 2
            bigger_med = half - smaller_med

            # FIX 3: sentinel values
            s_left  = smaller[smaller_med - 1] if smaller_med > 0 else float("-inf")
            s_right = smaller[smaller_med] if smaller_med < smaller_length else float("inf")

            b_left  = bigger[bigger_med - 1] if bigger_med > 0 else float("-inf")
            b_right = bigger[bigger_med] if bigger_med < len(bigger) else float("inf")

            # FIX 4: correct partition condition
            if s_left <= b_right and b_left <= s_right:
                if total % 2 == 0:
                    return (max(s_left, b_left) + min(s_right, b_right)) / 2
                else:
                    return min(s_right, b_right)

            if s_left > b_right:
                r = smaller_med - 1
            else:
                l = smaller_med + 1

"""
Goal: find median between 2 sorted arrays. e.g if sorted = 12345, median = 3
- identify if total = odd or even. 
    - if odd, just return min of right partition
    - if even, return avg of max(left partition) and min(right partition)
- find median of smaller array (limiting factor) and use it to find median of sorted array (half - medsmaller)
- check if rightmost of left partitions are smaller than leftmost of right partitions
    - if not, adjust smaller median and recalculate
- return as mentioned above
"""