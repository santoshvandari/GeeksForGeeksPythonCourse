#{ 
 # Driver Code Starts
#Initial Template for Python 3

class FibO:
    def __init__(self, X, Y, Z):
        self.x = X
        self.y = Y
        self.z = Z
    def fiboSum(self, obj):
        self.x += obj.x
        self.y += obj.y
        self.z += obj.z
    def getCoord(self):
        print(self.x, self.y, self.z)
    def deepCopy(self, obj):
        self.x, self.y, self.z = obj.x, obj.y, obj.z
        

# } Driver Code Ends
#User function Template for python3






def nthFibO(n, obj1, obj2):
    ##Your code here
    if n==1:
        return obj1
    if n==2: 
        return obj2
    
    for i in range(3,n+1):
        temp = obj1.fiboSum(obj2)
        obj1=obj2
        obj2=obj2.deepCopy(temp)
    return obj2
    
    

#{ 
 # Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases > 0):
        
        xyz1 = [int(i) for i in input().split()]
        x1 = xyz1[0]
        y1 = xyz1[1]
        z1 = xyz1[2]
        
        xyz2 = [int(i) for i in input().split()]
        x2 = xyz2[0]
        y2 = xyz2[1]
        z2 = xyz2[2]
        
        n = int(input())
        obj1 = FibO(x1,y1,z1)
        obj2 = FibO(x2,y2,z2)
        (nthFibO(n, obj1, obj2).getCoord())
        
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends