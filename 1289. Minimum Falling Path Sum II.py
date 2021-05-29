class Solution(object):
    def minFallingPathSum(self, A):
        
        if A == [] or A == [[]]: 
            return 0
        
        if len(A) == 1: 
            return min(A[0])
        
        m = len(A)+2   
        dp = [[0 for i in range(m)] for j in range(m)]
    
        for i in range(1,len(dp)-1):
            for j in range(1,len(dp)-1):
                dp[i][j] = A[i-1][j-1]
                
        for i in range(1,len(dp)):
            temp = sorted(dp[i-1])
            
            for j in range(1,len(dp)-1):
                if dp[i-1][j] == temp[0]: 
                    dp[i][j] += temp[1]
                else: 
                    dp[i][j] += temp[0]
            dp[i][0] = float('Inf')
            dp[i][-1] = float('Inf')
        
        return min(dp[-2])