#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def aweSum(A, B):
    ##Your code here
    sum = A+B
    if(sum >=20 and sum <=40):
        return 42
    return sum

#{ 
 # Driver Code Starts.





def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        A = int(input())
        B = int(input())
        print(aweSum(A, B))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends