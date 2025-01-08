#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3



def copyCat(str):
    ##Your code here
    newstr=str[-2::]
    return newstr*3

#{ 
 # Driver Code Starts.





def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(copyCat(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends