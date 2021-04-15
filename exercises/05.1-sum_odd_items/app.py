arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
largo= len(arr)
sumOdds=[]
#print(largo)
for i in range(0,largo):
    if arr[i]%2 != 0:
        sumOdds=sumOdds+[arr[i]]
print(sum(sumOdds))

        
