def nearestPower(A, B):
    ##Your code here
    ##return the closest power
    close=1
    mindiff=abs(close - B)
    power=1
    while True:
        current_x=A**power
        currdiff=abs(current_x-B)
        if(current_x == B):
            close=current_x
            break
        
        elif(currdiff<mindiff):
            close=current_x
            mindiff=currdiff
            
        else:
            break
        
        if current_x > B:
            break
        power=power+1
        
    return close

#{ 
 # Driver Code Starts.


import math

    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        A = int(input())
        B = int(input())
        print(nearestPower(A, B))
        testcases-=1
        


if __name__=='__main__':
    main()
# } Driver Code Ends