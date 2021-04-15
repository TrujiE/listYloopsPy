
tasks = [
	{ "label": 'Eat my lunch', "done": True },
	{ "label": 'Make the bed', "done": False },
	{ "label": 'Have some fun', "done": False },
	{ "label": 'Finish the replits', "done": False },
	{ "label": 'Replit the finishes', "done": True },
	{ "label": 'Ask for a raise', "done": False },
	{ "label": 'Read a book', "done": True },
	{ "label": 'Make a trip', "done": False }
]

#transformedData= list(map(lambda persona: persona.values(), incomingAJAXData))
#Your code go here:
def obtiene_true(nombre):
    #print(nombre)
    return nombre == True

<<<<<<< HEAD
val_done=list(filter(lambda persona: persona["done"], tasks)) 
resulting_true= list(filter(obtiene_true, val_done))
print(val_done)
=======

resulting_names= list(map(lambda falso: falso.items(), tasks))
print(resulting_names)







>>>>>>> 22d351d5ed44803f5f5f307f8ee2f3ef336e78f1
