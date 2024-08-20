

def check(s):
    '''It must start with a 4,5 or 6 '''
    if (s[0]!=4 or s[0]!=5 or s[0]!=6):
        return "Invalid"
    
    '''1/ It must contain exactly 16 digits.'''
    if len(s.replace("-", ""))!= 16:
        return "Invalid"
    
    '''2/ It must only consist of digits (0-9).'''
    for i in range(len(s)):
        if s[i]=="-":
            continue
        if not s[i].isdigit():
            return "Invalid"
    
    '''3/ It may have digits in groups of 4, separated by one hyphen "-".'''
    if "-" in s:
        groups = s.split("-")
        if len(groups) != 4 or any(len(group) != 4 for group in groups):
            return "Invalid"
    # d=0
    # for i in range(len(s)):
    #     if (s[i]=="-" and d!=4):
    #         return "Invalid"
    #     elif (s[i]=="-" and d==4):
    #         d=0
    #     else:
    #         d+=1
    
    '''4/ It must NOT use any other separator like ' ' , '_', etc.'''
    if (" " in s or "_" in s):
        return "Invalid"
    
    '''5/ It must NOT have 4 or more consecutive repeated digits.'''
    c=0
    cc=s.replace("-", "")
    for i in range(len(cc)-1):
        if (cc[i]!=cc[i+1]):
            c=0
        else:
            c+=1
        if c==3:
            return "Invalid"
        
    return "Valid"
    
n=input("Enter ur 16 digit n0: ")
for i in range(int(n)):
    s=input()
    if (check(s)):
        print("Valid")
    else:
        print("Invalid")

