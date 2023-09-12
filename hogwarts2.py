# Dictionary's values are stored in {}.
# To make it look neat, store variables in columns.

students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Gryffindor"
}

for student in students:
    print(student, students[student], sep=", ")