people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
people_temp=[]
people_temp=people
def deletePerson(person_name):
    #Your code go here:
    for x,y in enumerate(people_temp):
        if y == person_name:
            people_temp.pop(x)
 
    return people_temp
   

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))