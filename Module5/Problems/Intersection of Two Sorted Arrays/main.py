#User function Template for python3

# Done With the help of ChatGpt


class Solution:
    #Function to return a list containing the intersection of two arrays.
    def intersection(self, arr1, arr2):
        i,j=0,0
        n,m=len(arr1),len(arr2)
        result=[]
        
        while i<n and j<m:
            if i>0 and arr1[i]==arr1[i-1]:
                i+=1
                continue
            
            if arr1[i]==arr2[j]:
                result.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i] < arr2[j]:
                i+=1
            else:
                j+=1
        return result
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        l = ob.intersection(arr1, arr2)
        if (len(l) > 0):
            print(*l)
        else:
            print("[]")
        print("~")

# } Driver Code Ends