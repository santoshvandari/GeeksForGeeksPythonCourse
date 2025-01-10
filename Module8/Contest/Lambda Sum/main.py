#{ 
 # Driver Code Starts
#Initial Template for Python 3



# } Driver Code Ends
#User function Template for python3


##Write your lambda function here that will be assigned to sum
sum = lambda x,y:x+y



#{ 
 # Driver Code Starts.


def main():
    testcases = int(input()) #testcases
    while(testcases>0):
        X = int(input())
        Y = int(input())
        
        print(sum(X, Y))
        
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends