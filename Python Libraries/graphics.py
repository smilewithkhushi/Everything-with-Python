import matplotlib.pyplot as plt

print("\n \t PLOTTING A PIE CHART WITH VALUES ENTERED BY USER")
data=eval(input("Enter the data here : "))
labels=eval(input("Enter the labels for chart : "))
plt.pie(data, labels=labels, autopct='%.2f')
plt.title('PIE CHART')
plt.show()


print("\n \t PLOTTING A HISTOGRAM WITH VALUES ENTERED BY USER")
data=eval(input("Enter the data here : "))
plt.hist(data)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('HISTOGRAM')
plt.xlim(min(data)-1, max(data)+1)      #setting the limits of x axis
plt.show()


print("\n \t PLOTTING A HISTOGRAM WITH PREDEFINED VALUES")
data=[5,10,23,12,33,54,23,12,45,66,78,65,34,23]
plt.hist(data)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('HISTOGRAM')
plt.xlim(min(data)-1, max(data)+1)      #setting the limits of x axis
plt.show()

print("\n \t PLOTTING A LINE WITH USING LABELS & GRID")
a=[1,2,3,4,5]
b=[2,4,6,8,10]
plt.plot(a,b,'r*--', markersize=10.5, linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X vs X*X')
plt.grid()
plt.show()

print("\n \t PLOTTING A LINE WITH SETTING AXIS PARAMETERS")
a=[2,4,6,8,10,12]
b=[3,6,9,12,15,18]
plt.plot(a,b,'r*--', markersize=10.5, linewidth=2)
plt.axis([1,11,2,12])
plt.show()


print("\n \t PLOTTING A LINE WITH ASTERICKS AND DASHES")
plt.plot(a,b,"r*--")
plt.show()

print("\n \t PLOTTING A LINE ON THE GRAPH")
x=[2,4,6,8,10]
y=[3,6,9,12,15]
plt.plot(x,y)
plt.show()

print("\n \t PLOTTING SEVERAL POINTS ON THE GRAPH")
plt.plot(x,y,'ro')
plt.show()

print("\n \t PLOTTING A POINT WITH COLOR AND SHAPE")
plt.plot(3,5,'ro')      #red with dot/circle
plt.show()

plt.plot(3,5,'b+')      #blue with plus 
plt.show()

print("\n \t PLOTTING A POINT")
plt.plot(3,2)
plt.show()




