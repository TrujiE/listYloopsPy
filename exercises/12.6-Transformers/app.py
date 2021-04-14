incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
#def my_var(ent):
transformedData= list(map(lambda persona: persona.values(), incomingAJAXData))
for x in transformedData:
    print(' '.join(map(str,x)))    



