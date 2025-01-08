#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def realSum(mylist):
    ##Your code here
    i = 0
    sum = 0
    while i<len(mylist):
        if mylist[i] == 7:
            i+=2
            continue
        sum+=mylist[i]
        i+=1
    return sum


#{ 
 # Driver Code Starts.




def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        
        mylist = [int(x) for x in input().split()]
        print(realSum(mylist))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends