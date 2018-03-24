n = int(input())
i=0
l1 = []
while (i<n):
    a = input()
    l1.append(a)
    i=i+1

q = int(input()) 
j= 0
l2 = []
while(j<q):
    b = input()
    l2.append(b)
    j=j+1

print(l1 )
print()
print(l2)

c =0
for i in l2:    
    for j in l1:
         if( l2[i] == l1[j] ):
                c = c+1
    print(c)
       
        
    
        
    

    
    
    
    
    
