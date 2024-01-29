from faker import Faker
import random

fake = Faker()
print(fake.name())

students = []


def generate_student():
    for i in range(10):
        student = {
            "name": fake.name(),
            "age": random.randint(18, 65),
            "grade": random.randint(90, 100),
            "major": random.choice(["computer science", "math", "physics", "chemistry", "bio"]),
            "is_international": random.choice([True, False]),
            
        
    }
    students.append(student)
    print(student)
    
name = []    
for student in students:    
    name.append(student["name"])
print(name)
    




#duplicate_count = {name: first_names.count(name)}
#print(duplicate_count)


