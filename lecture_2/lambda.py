fullNames = [
    {"fName": "Manoj", "lName": "Kumar"},
    {"fName": "Monika", "lName": "Baghel"},
    {"fName": "Aman", "lName": "Singh"},
]

# replace this by lambda
# def fullName(name):
#     return name["fName"]

fullNames.sort(key=lambda fullName: fullName["fName"])

print(fullNames)

# lambda argument:result
