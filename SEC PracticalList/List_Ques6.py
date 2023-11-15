#question 6 : list programs

def evenTuple(t):
    temp=[]
    for i in t:
        if (i%2==0):
            temp.append(i)
    res=tuple(temp)
    return res
    
t1=(1,2,5,7,9,2,4,6,8,10)
tnew=evenTuple(t1)
print("-> Tuple t1 : ", t1)
print("-> Tuple with even values from t1 : ", tnew)
t2=(11,13,15)
print("-> Tuple t2 : ", t2)
print("-> t1 contactenated with t2 : ", t1+t2)
print("-> Max value from t1 : ", max(t1))
print("-> Min value from t1 : ", min(t1))
