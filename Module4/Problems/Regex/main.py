
import re ##import re module to use regex

# } Driver Code Ends
#User function Template for python3



def numberMatcher(str):
    pat=re.compile("\d+")
    match=re.findall(pat,str)#ind all finds all the matched texts and returns a list
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")


#{ 
 # Driver Code Starts.

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        numberMatcher(str)
        print()
        testcases -= 1
        


        print("~")
if __name__=='__main__':
    main()
# } Driver Code Ends