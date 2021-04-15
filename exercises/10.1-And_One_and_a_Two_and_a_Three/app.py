contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
lista= contact.items()
for x in lista:
    print(' : '.join(map(str,x)))

