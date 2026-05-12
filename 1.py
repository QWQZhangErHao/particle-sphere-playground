a = ''
count = 0
for i in range(1,2027):
    a +=  str(i)
    if int(a)%26 ==0:
        count+=1
    
print(count)