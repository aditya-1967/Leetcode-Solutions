# 632. Smallest Range Covering Elements from K Lists
# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        
        pq = []
        ma = 0
        
        for i in range(n):
            heappush(pq, (nums[i][0] , i, 0))
            ma = max(ma , nums[i][0])
        
        ans = [pq[0][0] , ma]
        while True:
            
            _,i,j = heappop(pq)
            
            
            if j == len(nums[i])-1:
                break
                
            next_num = nums[i][j+1]
            
            ma = max( ma , next_num)
            
            heappush(pq,(next_num, i , j+1))
            
            if ma-pq[0][0] < ans[1] - ans[0]:
                ans= [pq[0][0], ma]
        return ans
