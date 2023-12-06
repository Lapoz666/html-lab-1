num=int(input("Enter a Number :" ))
list_div=[]
for i in range(1,num+1):
    if(num % i == 0):
        list_div.append(i)

print(list_div)    
        
