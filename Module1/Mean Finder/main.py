#User function Template for python3

def mean(D,M):
    ##Your code here
    return (((3*M)+D)// 4)
    

#{ 
 # Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        D = int(input()) ##taking d as input
        M = int(input()) ## taking mean of 3 numbers
        print(mean(D, M))
        testcases-=1
        


if __name__=='__main__':
    main()