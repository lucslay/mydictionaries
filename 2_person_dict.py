person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
print(type(person['children']))
print(person['children'][1])
print(person['pets']['cat'])

for x in person:
    print(person)

#for names of pets
