mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below:
#
largo= len(mix)
#print(largo)
#def tipo_valores():
for largo in range(0,largo,1):
    tipo=type(mix[largo])
    print(tipo)

