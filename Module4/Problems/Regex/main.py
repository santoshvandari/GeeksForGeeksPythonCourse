import re
def numberMatcher(str):
    pat=re.compile("[0-9]")
    match=re.findall(pat,str) #ind all finds all the matched texts and returns a list
    print(match)
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")

str = "asdasd123asmdasdk34234kfdsd34sdfk5"
print()
numberMatcher(str)
print()