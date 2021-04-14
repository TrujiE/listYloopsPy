theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def lista(booleanos):
    if booleanos == 0:
        print("woko")
    elif booleanos ==1:
        print("wiki")

resultado= list(map(lista, theBools))
