#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def isNeighbour(N):
    ##Your code here
    reminder = N%10
    difference=reminder
    if reminder > 2:
        difference = abs((10-reminder))
    if(difference<=2):
        return True
    else:
        return False



#{ 
 # Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        N = int(input())
        print(isNeighbour(N))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends