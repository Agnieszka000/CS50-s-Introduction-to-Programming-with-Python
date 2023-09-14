# List with dictionaries for every student:

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None} # When there's no value to the key we use "None".
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")