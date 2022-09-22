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

Given N doors and N persons. The doors are numbered from 1 to N and persons are given id’s numbered from 1 to N. Each door can have only two statuses i.e. open (1) or closed (0) . Initially all the doors have status closed. Find the final status of all the doors, when all the persons have changed the status of the doors of which they are authorized. i.e. if status open then change the status to closed and vice versa. A person with id ‘i’ is authorized to change the status of door numbered ‘j’ if ‘j’ is a multiple of ‘i’.
Note: A person has to change the current status of all the doors for which he is authorized exactly once.

 

Example 1:

Input:
N = 3
Output:
1 0 0 
Explanation:
Initiall status of rooms - 0 0 0. 
Person with id 2 changes room 2 to open,
i.e. (0 1 0). Person with id 1 changes
room 1, 2, 3 status (1 0 1).
Person with id 3 changes room 3
status i.e. (1 0 0).
Example 2:

Input:
N = 2
Output:
1 0
Explanation:
Initiall status of rooms - 0 0. 
Person with id 2 changes room 2 to open,
i.e. (0 1). Person with id 1 changes
room 1, 2 status (1 0).


'''
