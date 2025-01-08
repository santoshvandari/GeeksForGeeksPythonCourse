#User function Template for python3


def imgExtracter(str):
    ##Your code here
    #Print the output
    imgpart=str.split("<img src='")[1].split("'")[0]
    print(imgpart)
    return


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import re





def main():
    testcases=int(input()) #testcases
    while(testcases > 0):
        str = input()
        imgExtracter(str)
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends