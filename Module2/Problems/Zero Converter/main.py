#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def pos(n):
    ## Write the code
    i=n-1
    while(i>=0):
        print(i,end=" ")
        i-=1
    
def neg(n):
    ##Write the code
    i=n
    while(i<=0):
        print(i,end=" ")
        i+=1        

#{ 
 # Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n = int(input())
        if(n > 0):
            pos(n)
        elif(n < 0):
            neg(n)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        


        print("~")
if __name__=='__main__':
    main()
# } Driver Code Ends