#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def cat_hat(str):
  ##your code here##
  catcount = str.count("cat")
  hatcount = str.count("hat")
  if(catcount==hatcount):
      return True
  else: 
        return False
  ##You need to write complete code this time 


#{ 
 # Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(cat_hat(str))
        testcases-=1
        


        print("~")
if __name__=='__main__':
    main()
# } Driver Code Ends