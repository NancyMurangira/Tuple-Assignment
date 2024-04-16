#creating a tuple
country = ("Rwanda", "Malawi", "Ethiopia", "Uganda")
print(country)

# Creating a tuple with one element
names = ("Liza",)
#print(names)

#Adding an item in a tuple
country = ("Rwanda", "Malawi", "Ethiopia", "Uganda")
TupleToList = list(country)
TupleToList.append("Kenya")
country = tuple(TupleToList)
print(country)

#Remove an item in a tuple
TupleToList.remove("Ethiopia")
country = tuple(TupleToList)
print(country)

#Deleting an item in a tuple
#del country

