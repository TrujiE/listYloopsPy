
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def obtiene_mayuscula(nombre):
    return nombre.startswith("R")

resulting_names= list(filter(obtiene_mayuscula, all_names))
print(resulting_names)




