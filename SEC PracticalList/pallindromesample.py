
    if (l%2!=0):   #odd length test
        temp=0 
        rem=int((temp-1)/2)
        for i in range(rem):
            if a[i]==a[l-1]:
                temp+=1
        rem=int(temp/2)
        if (temp==rem):
            result=1
        else:
            result=0
        
    else: #even length test (l!2==0)
        temp=0
        rem=int(temp/2)
        for i in range(rem):
            if a[i]==a[l-1]:
                temp+=1
        if (temp==rem):
            result=1
        else:
            result=0
    return result      
    
