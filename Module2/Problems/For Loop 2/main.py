
def stringJumper(str):
    strlen= len(str)
    for i in range(0,strlen,2): ## from 0 to length of str and skip 2
        print(str[i], end="") ##printing character and separating characters by nothing ##printing character and separating characters by nothing



#{ 
 # Driver Code Starts.



def main():
    testcases = int(input()) #testcases
    while(testcases>0):
        str = (input())
        stringJumper(str)
        print()##separating testcases outputs by newline