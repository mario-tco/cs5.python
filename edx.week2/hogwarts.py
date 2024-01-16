# Dictionary example
studentsDictionary = {
    "Panone": "Slytherin",
    "Pazuzu": "Gryffindor",
    "Dobbo": "Hufflepuff"
}

for student in studentsDictionary:
    print(student, studentsDictionary[student], sep=", ")

# List of Dictionaries
studentsList = [
    {"name": "Panone", "house": "Slytherin", "patronus": "Hehe"},
    {"name": "Pazuzu", "house": "Gryffindor", "patronus": "Mono"},
    {"name": "Dobbo", "house": "Hufflepuff", "patronus": None}
]

for student in studentsList:
    print(student["name"], student["house"], student["patronus"], sep=", ")