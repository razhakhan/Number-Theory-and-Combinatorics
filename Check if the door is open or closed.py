'''

door is open or 1 only when the id has odd number of divisors
and closed for even number of divisors

no of divisors is odd only for perfect squares

'''

#User function Template for python3

class Solution:
    def checkDoorStatus(self, N):
        import math
        arr=[0]*N
        for i in range(1,N+1):
            if (math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i))):   # perfect square or not
                arr[i-1]=1
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ptr = ob.checkDoorStatus(N)
        print(*ptr)
# } Driver Code Ends

'''

Examples : 
 

Input  : n = 10      
Output : Even

Input:  n = 100
Output: Odd

Input:  n = 125
Output: Even

'''
