x=[2,5]
y=[6,7]
def dot(x,y):
   s=0
   for i in range(0,len(x)):
    for j in range(0,len(y)):
       if i==j:
         s=s+x[i]*y[j]
   return s
print(dot(x,y))
